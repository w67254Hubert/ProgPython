import tkinter as tk
from tkinter import ttk, messagebox
from statsmodels.tsa.statespace.sarimax import SARIMAX
from ttkthemes import ThemedTk
import requests
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.widgets import SpanSelector
import numpy as np
import threading
import datetime
from scipy.optimize import minimize
import json
import os  # Importujemy moduł os
###
####################################
# Konfiguracja kluczowych danych
####################################
CRYPTOCOMPARE_API_KEY = ''
PORTFOLIO_FILE = "portfolio.json"  # Nazwa pliku do zapisu portfela


####################################
# Klasa: Portfel kryptowalut
####################################
class Portfolio:
    def __init__(self):
        self.assets = []  # Lista aktywów w portfelu
        self.totalValue = 0
        self.historicalValues = {}  # Dict z historycznymi danymi dla kazdej kryptowaluty

    def addAsset(self, cryptoName, amount, price):
        # Dodaje kryptowalutę do portfela.
        self.assets.append({
            'cryptoName': cryptoName,
            'amount': amount,
            'price': price
        })
        self.calculateTotalValue()

    def removeAsset(self, cryptoName):
        # Usuwa kryptowalutę z portfela, poprzez iterazje po liście i nie dodanie wybranej krypto do nowej tablicy
        self.assets = [asset for asset in self.assets if asset['cryptoName'] != cryptoName]
        self.calculateTotalValue()

    def calculateTotalValue(self):
        # Oblicza całkowitą wartość portfela i aktualizuje totalValue.
        self.totalValue = sum(asset['amount'] * asset['price'] for asset in self.assets)

    def updatePrices(self):
        # Aktualizuje ceny kryptowalut w portfelu.
        for asset in self.assets:
            asset['price'] = Portfolio.getCurrentPrice(asset['cryptoName'], CRYPTOCOMPARE_API_KEY)
        self.calculateTotalValue()  # Aktualizacja wartości portfela  po zmianie cen

    def predictPortfolioValue(self, days, sarimaOrder=(1, 1, 1), sarimaSeasonalOrder=(1, 1, 1, 7),
                             historicalLimit=30):
        # Generuje prognozę wartości portfela na określoną liczbę dni przy użyciu modelu SARIMAX.
        if not self.assets:
            print("Portfel jest pusty. Nie można prognozować.")
            return [self.totalValue] * days

        # Agregacja danych historycznych do wartości portfela w czasie
        portfolioHistoricalValues = self.fetchAndAggregateHistoricalData(historicalLimit)

        if len(portfolioHistoricalValues) < 30:
            print("Zbyt mało danych historycznych do prognozowania SARIMAX. Zamiana na prosty model.")
            totalValue = self.totalValue
            return list(map(lambda day: totalValue * (1 + 0.01 * day), range(1, days + 1)))

        # Ekstrakcja wartości historycznych portfela
        values = [value for _, value in portfolioHistoricalValues]

        # Wykorzystanie funkcji forecastPrices do prognozowania
        predictedMean, _ = Portfolio.forecastPrices(values, days)  # Dodano _ ponieważ drugi element zwracany przez forecastPrices nie jest potrzebny

        if predictedMean is None:
            print("Błąd prognozowania SARIMAX. Zamiana na prosty model.")
            totalValue = self.totalValue
            return list(map(lambda day: totalValue * (1 + 0.01 * day), range(1, days + 1)))

        return list(predictedMean)

    def fetchAndAggregateHistoricalData(self, limit):
        # Pobiera i agreguje dane historyczne dla kryptowalut w portfelu.
        allHistoricalData = {}
        for asset in self.assets:
            cryptoName = asset['cryptoName']
            try:
                dates, prices = Portfolio.getHistoricalData(cryptoName, CRYPTOCOMPARE_API_KEY, limit=limit)
                if dates and prices:
                    allHistoricalData[cryptoName] = sorted(zip(dates, prices))  # Sortowanie po dacie
                else:
                    print(f"Nie udało się pobrać danych historycznych dla {cryptoName}.")
                    allHistoricalData[cryptoName] = []
            except Exception as e:
                print(f"Błąd podczas pobierania danych historycznych dla {cryptoName}: {e}")
                allHistoricalData[cryptoName] = []

        # Znajdź wszystkie unikalne daty
        allDates = set()
        for cryptoName in allHistoricalData:
            if allHistoricalData[cryptoName]:
                for date, _ in allHistoricalData[cryptoName]:
                    allDates.add(date)
        sortedDates = sorted(list(allDates))

        # Oblicz wartość portfela dla każdej daty
        portfolioValues = []
        for date in sortedDates:
            totalValueForDate = 0
            for asset in self.assets:
                cryptoName = asset['cryptoName']
                amount = asset['amount']
                # Znajdź cenę dla danej daty (jeśli istnieje)
                priceForDate = None
                if cryptoName in allHistoricalData and allHistoricalData[cryptoName]:
                    for d, prise in allHistoricalData[cryptoName]:
                        if d <= date:  # Użyj ostatniej dostępnej ceny przed daną datą
                            priceForDate = prise
                        else:
                            break  # Data jest późniejsza, szukamy dalej
                # Dodaj do wartości portfela
                if priceForDate is not None:
                    totalValueForDate += amount * priceForDate
            portfolioValues.append((date, totalValueForDate))
        return portfolioValues

    def optimizePortfolio(self):
        # Analizuje i sugeruje optymalizację portfela na podstawie alokacji i zmienności,
        # w tym implementacja optymalizacji Markowitza

        if not self.assets:
            return ["Portfel jest pusty. Nie można przeprowadzić optymalizacji."]

        historicalData = {}
        for asset in self.assets:
            dates, prices = Portfolio.getHistoricalData(asset['cryptoName'], CRYPTOCOMPARE_API_KEY, limit=100)
            if not prices or len(prices) < 2:  # Sprawdzamy, czy są dane i wystarczająca liczba danych do obliczeń
                return [f"Brak wystarczających danych historycznych dla {asset['cryptoName']}."]
            historicalData[asset['cryptoName']] = prices

        if not historicalData:
            return ["Brak danych do optymalizacji."]

        # Optymalizacja Markowitza
        try:
            optimizedWeights = self.markowitzOptimization(historicalData)
            if optimizedWeights is not None:
                suggestions = self.generateMarkowitzSuggestions(optimizedWeights)
            else:
                suggestions = ["Nie można zoptymalizować portfela. Błąd podczas obliczeń."]
        except Exception as e:
            suggestions = [f"Nie można zoptymalizować portfela. Błąd: {e}"]

        return suggestions

    def markowitzOptimization(self, historicalData):
        # Optymalizacja portfela Markowitza.

        prices = np.array(list(historicalData.values()))
        returns = np.diff(prices, axis=1) / prices[:, :-1]  # return z cen w poszczególnych kolumnach
        mean_returns = np.array(list(map(np.mean, returns)))  # sredni zwrot aktywów
        covariance_matrix = np.cov(returns)  # macierz kowariancji

        num_assets = len(self.assets)

        def portfolioVariance(weights):
            return np.dot(weights.T, np.dot(covariance_matrix, weights))

        def negPortfolioReturn(weights):
            return -np.dot(weights.T, mean_returns)  # - by znaleźć max zwrot

        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})  # suma wag ma sie równac 1
        bounds = tuple((0, 1) for _ in range(num_assets))  # 0 do 1 zakres wagi aktywów
        initial_weights = np.array([1 / num_assets] * num_assets)  # wagi startowe

        optimizedResult = minimize(
            negPortfolioReturn,
            initial_weights,
            method='SLSQP',
            bounds=bounds,
            constraints=constraints
        )
        if optimizedResult.success:
            return optimizedResult.x
        else:
            return None

    def generateMarkowitzSuggestions(self, optimizedWeights):
        # Generuje sugestie na podstawie optymalizacji Markowitza.

        suggestions = []
        for i, asset in enumerate(self.assets):
            currentWeight = self.assets[i]['amount'] * self.assets[i]['price'] / self.totalValue if self.totalValue > 0 else 0
            optimizedWeight = optimizedWeights[i]
            difference = optimizedWeight - currentWeight
            if difference > 0.02:  # zmiana conajmniej o 2%
                suggestions.append(
                    f"Zwiększ udział {asset['cryptoName']} do {optimizedWeight * 100:.2f}% (z obecnych {currentWeight * 100:.2f}%)."
                )
            elif difference < -0.02:
                suggestions.append(
                    f"Zmniejsz udział {asset['cryptoName']} do {optimizedWeight * 100:.2f}% (z obecnych {currentWeight * 100:.2f}%)."
                )
        if not suggestions:
            suggestions.append("Portfel jest zoptymalizowany zgodnie z modelem Markowitza.")
        return suggestions

    def to_dict(self):
        """Konwertuje obiekt Portfolio na słownik."""
        return {
            'assets': self.assets,
            'totalValue': self.totalValue,
            'historicalValues': self.historicalValues
        }

    @classmethod
    def from_dict(cls, data):
        """Tworzy obiekt Portfolio ze słownika."""
        portfolio = cls()
        # portfolio.assets = data.get('assets', [])
        # portfolio.totalValue = data.get('totalValue', 0)
        portfolio.historicalValues = data.get('historicalValues', {})
        if 'assets' in data:
            for asset_data in data['assets']:
                portfolio.addAsset(asset_data['cryptoName'], asset_data['amount'], asset_data['price'])
        return portfolio

    ####################################
    # Funkcje pomocnicze
    ####################################
    @staticmethod
    def get_crypto_list(api_key):
        # Pobiera listę kryptowalut dostępnych w API CryptoCompare.
        url = 'https://min-api.cryptocompare.com/data/all/coinlist'
        try:
            response = requests.get(url, params={'api_key': api_key})
            response.raise_for_status()
            data = response.json()
            return sorted(coin['Symbol'] for coin in data['Data'].values())
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Błąd", f"Błąd API podczas pobierania listy kryptowalut: {e}")
            return []

    @staticmethod
    def validateSarimaParams(order, seasonal_order):
        # Sprawdza, czy parametry SARIMA są poprawne.
        if not isinstance(order, tuple) or len(order) != 3:
            raise ValueError(f"Nieprawidłowy format 'order': {order}. Parametr musi być krotką trzech liczb.")
        if not isinstance(seasonal_order, tuple) or len(seasonal_order) != 4:
            raise ValueError(
                f"Nieprawidłowy format 'seasonal_order': {seasonal_order}. Parametr musi być krotką czterech liczb.")

        for param in order:
            if not isinstance(param, int) or param < 0:
                raise ValueError(
                    f"Nieprawidłowa wartość  {param} w 'order'. Wartości muszą być dodatnimi liczbami całkowitymi.")

        for param in seasonal_order:
            if not isinstance(param, int) or param < 0:
                raise ValueError(
                    f"Nieprawidłowa wartość {param} w 'seasonal_order'. Wartości muszą być dodatnimi liczbami całkowitymi.")

    @staticmethod
    def getCurrentPrice(symbol, api_key):
        # Pobiera aktualną cenę kryptowaluty.
        url = 'https://min-api.cryptocompare.com/data/price'
        params = {'fsym': symbol, 'tsyms': 'USD', 'api_key': api_key}
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json().get('USD', 0)
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Błąd", f"Błąd API podczas pobierania ceny {symbol}: {e}")
            return 0

    @staticmethod
    def getHistoricalData(symbol, api_key, limit=30):
        # Pobiera historyczne dane cenowe dla kryptowaluty.
        url = 'https://min-api.cryptocompare.com/data/v2/histoday'
        params = {'fsym': symbol, 'tsym': 'USD', 'limit': limit, 'api_key': api_key}
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json().get('Data', {}).get('Data', [])
            dates = [datetime.datetime.fromtimestamp(item['time']) for item in data]
            prices = [item['close'] for item in data]

            return dates, prices
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Błąd", f"Błąd API podczas pobierania danych historycznych {symbol}: {e}")
            return [], []

    @staticmethod
    def forecastPrices(prices, days=7):
        # Prognozuje ceny kryptowaluty na podstawie historycznych danych za pomocą modelu SARIMA.
        try:

            Portfolio.validateSarimaParams(order=(1, 1, 1), seasonal_order=(1, 1, 1, 7))
            model = SARIMAX(prices, order=(1, 1, 1), seasonal_order=(1, 1, 1, 7), enforce_stationarity=False,
                            enforce_invertibility=False)
            model_fit = model.fit(disp=False)
            forecast = model_fit.get_forecast(steps=days)
            predicted_mean = forecast.predicted_mean
            conf_int = forecast.conf_int()
            return predicted_mean, conf_int

        except ValueError as e:
            messagebox.showerror("Błąd w generowaniu  SARIMA dla", f'{e}')
            return None, None
        except Exception as e:
            print(f"Błąd prognozowania SARIMA: {e}")
            return None, None

    @staticmethod
    def calculateMovingAverage(prices, window=7):
        # Oblicza średnią ruchomą.

        if len(prices) < window:
            return [np.nan] * len(prices)

        moving_average = np.convolve(prices, np.ones(window), 'valid') / window
        padding = [np.nan] * (window - 1)
        return padding + list(moving_average)


####################################
# Funkcje zapisu/odczytu portfela
####################################
def savePortfolio(portfolio, filename):
    # Zapisuje stan portfela do pliku JSON
    try:
        #Konwertuj aktywa na format, który można serializować do JSON
        assets_serializable = []
        for asset in portfolio.assets:
            assets_serializable.append({
            'cryptoName': asset['cryptoName'],
            'amount': asset['amount'],
            'price': asset['price']
        })

        with open(filename, 'w') as f:
            json.dump({'assets': assets_serializable}, f)  # Zapisz portfel jako słownik
        print("Portfel zapisany do pliku: ", filename)
    except Exception as e:
        print(f"Błąd podczas zapisywania portfela: {e}")


def loadPortfolio(filename):
    # Wczytuje stan portfela z pliku JSON
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                portfolio = Portfolio.from_dict(data)  # Używamy from_dict do utworzenia portfela
            print("Portfel wczytany z pliku: ", filename)
            return portfolio
        except Exception as e:
            print(f"Błąd podczas wczytywania portfela: {e}")
            return Portfolio()  # W przypadku błędu, zwróć nowy portfel
    else:
        print("Plik portfela nie istnieje. Tworzę nowy portfel.")
        return Portfolio()


####################################
# Funkcje GUI dzala
####################################
def createGui(portfolio, apiKey):
    root = ThemedTk(theme="arc")
    root.title("Portfel Krypto")
    root.geometry("900x700")

    def on_closing():
        # Funkcja wywoływana przy zamykaniu okna
        savePortfolio(portfolio, PORTFOLIO_FILE)
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)  # Wywołaj funkcję przy zamykaniu okna

    # Dodanie scrolla
    canvas = tk.Canvas(root)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    cryptoList = Portfolio.get_crypto_list(apiKey)

    # Ramka do dodawania kryptowalut
    frameAdd = ttk.LabelFrame(scrollable_frame, text="Dodaj kryptowalutę do portfela", padding=10)
    frameAdd.pack(fill="x", padx=10, pady=10)

    ttk.Label(frameAdd, text="Wybierz kryptowalutę:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    #cryptoVar = tk.StringVar() # Usunięto
    #cryptoDropdown = ttk.Combobox(frameAdd, textvariable=cryptoVar, state="normal") #Usunięto
    #cryptoDropdown.grid(row=0, column=1, padx=5, pady=5) #Usunięto
    #cryptoDropdown['values'] = cryptoList # Usunięto
    symbolEntry=ttk.Entry(frameAdd)
    symbolEntry.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(frameAdd, text="Ilość:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
    amountEntry = ttk.Entry(frameAdd)
    amountEntry.grid(row=1, column=1, padx=5, pady=5)

    def addCrypto():
        #symbol = cryptoVar.get() # Zmiana
        #cryptoVar = tk.StringVar() # Usunięcie
        #cryptoDropdown = ttk.Combobox(frameAdd, textvariable=cryptoVar, state="normal") #Usunięto
        #cryptoDropdown.grid(row=0, column=1, padx=5, pady=5) #Usunięto
        #cryptoDropdown['values'] = cryptoList # Usunięcie
        cryptoName = symbolEntry.get()
        symbol = cryptoName  # Zmiana - pobieranie z pola tekstowego
        amount = amountEntry.get()

        if not symbol or not amount:
            messagebox.showerror("Błąd", "Proszę uzupełnić wszystkie pola.")
            return

        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Ilość musi być większa od zera.")
            price = Portfolio.getCurrentPrice(symbol, apiKey)
            if price == 0:
                raise ValueError("Nie udało się pobrać ceny.")
            portfolio.addAsset(symbol, amount, price)
            updatePortfolioTable()
            messagebox.showinfo("Sukces", f"Dodano {amount} {symbol} do portfela.")
            #updateCryptoDropdown()  # Aktualizuj cryptoDropdown po dodaniu krypto
        except Exception as e:
            messagebox.showerror("Błąd", str(e))

    ttk.Button(frameAdd, text="Dodaj do portfela", command=addCrypto).grid(row=2, column=0, columnspan=2, pady=10)
    # Ramka portfela
    framePortfolio = ttk.LabelFrame(scrollable_frame, text="Twój portfel", padding=10)
    framePortfolio.pack(fill="both", expand=True, padx=10, pady=10)

    columns = ("crypto_name", "amount", "price", "value") # Usunięcie kolumny "chart"
    portfolioTable = ttk.Treeview(framePortfolio, columns=columns, show="headings", height=10)
    for col in columns:
        portfolioTable.heading(col, text=col.capitalize())
        portfolioTable.column(col, anchor="center")
    portfolioTable.pack(fill="both", expand=True)

    # Wywołanie funkcji, aby włączyć wyświetlanie button w wierszach Treeview
    def showChart():  # by zerowało cała  strukture canvas
        selected_item = portfolioTable.selection()[0]
        values=portfolioTable.item(selected_item)['values']
        symbol=values[0]
        
        thread = threading.Thread(target=updateChart,args=(symbol,))
        thread.start()
    
    buttonChart=ttk.Button(framePortfolio,text="Pokaż Wykres",command=showChart)
    buttonChart.pack()
    def removeSelectedCrypto():
        selectedItem = portfolioTable.selection()
        if not selectedItem:
            messagebox.showerror("Błąd", "Proszę wybrać kryptowalutę do usunięcia.")
            return

        cryptoName = portfolioTable.item(selectedItem, 'values')[0]
        portfolio.removeAsset(cryptoName)
        updatePortfolioTable()
        messagebox.showinfo("Sukces", f"Usunięto {cryptoName} z portfela.")
        #updateCryptoDropdown()  # Aktualizuj cryptoDropdown po usunięciu krypto

    ttk.Button(framePortfolio, text="Usuń wybraną kryptowalutę", command=removeSelectedCrypto).pack(pady=5)

    totalValueLabel = ttk.Label(framePortfolio, text="Wartość portfela: 0 USD")
    totalValueLabel.pack()

    def updatePortfolioTable():
        for row in portfolioTable.get_children():
            portfolioTable.delete(row)
        for asset in portfolio.assets:
            portfolioTable.insert("", "end", values=(
                asset['cryptoName'],
                asset['amount'],
                asset['price'],
                asset['amount'] * asset['price'],
            ))
        totalValueLabel.config(text=f"Wartość portfela: {portfolio.totalValue:.2f} USD")

    # Ramka wykresu
    frameChartContainer = ttk.Frame(scrollable_frame)  # kontrola na widget do umiescenia calego grafiki wykresu
    frameChartContainer.pack(fill="both", expand=True, padx=10, pady=10)

    frameChart = ttk.Frame(frameChartContainer)
    frameChart.pack(side="top", fill="both", expand=True, padx=10, pady=10)

    def updateChart(symbol):
       #symbol = cryptoVar.get() # Usunięto

        if not symbol:
            messagebox.showerror("Błąd", "Proszę wybrać kryptowalutę.")
            return

        # Definicja globalnego selektora, aby był widoczny w calej funkcji updateChart
        global spanSelector

        def fetchDataAndUpdateChart():
            dates, prices = Portfolio.getHistoricalData(symbol, apiKey, limit=30)

            if not prices:
                messagebox.showerror("Błąd", "Nie udało się pobrać danych historycznych.")
                return
            if not dates:
                messagebox.showerror("Błąd", "Nie udało się pobrać dat historycznych.")
                return

            figure = Figure(figsize=(8, 6), dpi=100)
            ax = figure.add_subplot(111)

            ax.plot(dates, prices, label="Cena", color="skyblue")

            movingAverage = Portfolio.calculateMovingAverage(prices)
            ax.plot(dates, movingAverage, label=f"SMA 7", color="darkred", linestyle='--')

            predictedMean, confInt = Portfolio.forecastPrices(prices, days=7)

            if predictedMean is not None and confInt is not None:
                forecastDays = [dates[-1] + datetime.timedelta(days=i + 1) for i in range(len(predictedMean))]
                ax.plot(forecastDays, predictedMean, label="Prognoza", linestyle="--", color='grey')

                # wyliczne przedziały ufność / wygenerowne zakres z lini prognozowania - i renderuje je pod grafe
                ax.fill_between(
                    forecastDays,
                    confInt[:, 0],
                    confInt[:, 1],
                    color="cornflowerblue",  # Zmiana koloru na intensywny niebieski
                    alpha=0.4,  # delikatnie mniejsza transparentność
                    label="Przedział ufności",
                )

            # ustawinia wykres / opis  grafu - i opisanych  elementów osi x/y

            ax.set_title(f"Cena {symbol}")
            ax.set_xlabel("Data")
            ax.set_ylabel("Cena [USD]")

            ax.legend()
            ax.grid(True)
            figure.autofmt_xdate()
            # zerowanie - widok - w widocznego w `Frame` (nie wywoal z Frame container tylko wykresy)
            for widget in frameChart.winfo_children():
                widget.destroy()

            canvasPlot = FigureCanvasTkAgg(figure, frameChart)
            canvasPlot.get_tk_widget().pack(fill="both", expand=True)
            canvasPlot.draw()

            # zakres generowania , - dynamiczne canvas do danych z y osi po  na canvas widok i selekcja po myszce
            def onselect(xmin, xmax):
                indmin, indmax = np.searchsorted(dates, (xmin, xmax))
                indmax = min(len(dates) - 1, indmax)

            # Generowanie wykresu po zdefiniowanym zakresem
                thisax = figure.add_subplot(111)
                # Generowanie wybranego podzbioru danych z tablicy
                thisax.plot(dates[indmin:indmax], prices[indmin:indmax], label='Cena', color='skyblue')

                thisax.set_title(f'Cena {symbol} ({xmin.strftime("%Y-%m-%d")} - {xmax.strftime("%Y-%m-%d")})')
                thisax.set_xlabel('Data')
                thisax.set_ylabel('Cena [USD]')
                # Wyświetlaj zmienione widoki na grafikę w obrębie ""
                thisax.legend()
                thisax.grid(True)
                canvasPlot.draw()

            # Sprawdz czy wykres zostal usunięty
            global spanSelector  # Upewnij się, że używasz globalnej zmiennej
            if 'spanSelector' in globals():
                try:
                    spanSelector = SpanSelector(ax, onselect, "horizontal", useblit=True)
                except Exception as e:
                    print(f"Błąd podczas tworzenia SpanSelector: {e}")
            else:
                print("SpanSelector już nie istnieje.")

        thread = threading.Thread(target=fetchDataAndUpdateChart)
        thread.start()

    frameButtons = ttk.Frame(
        frameChartContainer)  # umieszcze przyciski / do grafu poniżej wyliczonej ramki / kontenerem .
    frameButtons.pack(side="bottom", fill='x', padx=10, pady=10)

    #ttk.Button(frameButtons, text="Aktualizuj wykres", command=updateChart).pack(side="left", pady=10) #Usunięto

    def clearChart():  # by zerowało cała  strukture canvas
        for widget in frameChart.winfo_children():
            widget.destroy()

    ttk.Button(frameButtons, text="Wyczyść wykres", command=clearChart).pack(side="right",
                                                                               pady=10)  # buton widoczny i działa  odpowiednio po stronie   na ramce canvas , ma widok ale steruje czym innym i widok to canvas. (button na dole pod grafika)
    # Ramka prognoz wartości portfela
    framePredictions = ttk.LabelFrame(scrollable_frame, text="Prognoza wartości portfela", padding=10)
    framePredictions.pack(fill="both", expand=True, padx=10, pady=10)

    predictionsTable = ttk.Treeview(framePredictions, columns=("days", "value"), show="headings", height=3)
    predictionsTable.heading("days", text="Dni")
    predictionsTable.heading("value", text="Wartość (USD)")
    predictionsTable.column("days", anchor="center")
    predictionsTable.column("value", anchor="center")
    predictionsTable.pack(fill="both", expand=True)

    def updatePredictionsTable():
        for row in predictionsTable.get_children():
            predictionsTable.delete(row)

        def fetchPredictions():
            # portfolio.updatePrices() # Aktualizacja cen przed prognozowaniem -> usuniete
            predictedValues = portfolio.predictPortfolioValue(
                days=30)  # liniowe przewidywanie dla 3 liczb dni w kodzie do tabeli ui , wiec do niej beda zgenerowane z góry,
            # poprawne działanie i  dostarczania widoku do
            if predictedValues:
                for i, days in enumerate([1, 7,
                                          30]):  # zakres for ( bo tutaj sa problemy wyliczeń  z typów ` list`, - a ma byc do 3 el) / bo  kod na w  fetchPredictions ma poprawny i kontrolowany przez if  - by działalo, i miało konkretne wyliczenie na element.  Z listy "wyciętej" do elementu.
                    if len(predictedValues) > i:  # Dodane  dopasowanie elementu
                        predictionsTable.insert("", "end", values=(days, f"{predictedValues[i]:.2f}"))

        thread = threading.Thread(target=fetchPredictions)
        thread.start()

    ttk.Button(framePredictions, text="Aktualizuj prognozy", command=updatePredictionsTable).pack(pady=10)
    # Ramka optymalizacji portfela
    frameOptimization = ttk.LabelFrame(scrollable_frame, text="Optymalizacja portfela", padding=10)
    frameOptimization.pack(fill="both", expand=True, padx=10, pady=10)

    optimizationText = tk.Text(frameOptimization, height=5, wrap="word")
    optimizationText.pack(fill="both", expand=True)

    def updateOptimization():
        def fetchSuggestions():
            suggestions = portfolio.optimizePortfolio()
            optimizationText.delete("1.0", tk.END)
            if suggestions:
                optimizationText.insert(tk.END, "\n".join(suggestions))
            else:
                optimizationText.insert(tk.END, "Portfel jest zoptymalizowany.")

        thread = threading.Thread(target=fetchSuggestions)
        thread.start()

    ttk.Button(frameOptimization, text="Zaktualizuj optymalizację", command=updateOptimization).pack(pady=10)

    def refreshPortfolioValue():
        portfolio.updatePrices()
        updatePortfolioTable()
        root.after(10000, refreshPortfolioValue)

    # Inicjalizacja danych
    updatePortfolioTable()
    updatePredictionsTable()
    updateOptimization()
    refreshPortfolioValue()

    root.mainloop()


####################################
# Główna funkcja aplikacji
####################################
def main():
    # Uruchamia aplikację Crypto Portfolio Manager.
    portfolio = loadPortfolio(PORTFOLIO_FILE)  # Wczytujemy portfel z pliku
    createGui(portfolio, CRYPTOCOMPARE_API_KEY)


if __name__ == "__main__":
    main()