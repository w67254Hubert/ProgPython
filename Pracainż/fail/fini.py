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
import finnhub
#finhub nie jest odpowiedni z powodu braku informacji historycznych
###wdsaadas
# ===============================
# Konfiguracja kluczowych danych
# ===============================
API_KEY = ''  # Zastąp swoim kluczem API Finnhub
FINNHUB_CLIENT = finnhub.Client(api_key=API_KEY)

# ===============================
# Klasa: Portfel akcji
# ===============================
class Portfel:
    def __init__(self):
        self.assets = []  # Lista akcji w portfelu
        self.total_value = 0

    def add_asset(self, symbol, amount):
        """Dodaje akcje do portfela."""
        price = self.get_current_price(symbol)
        if price == 0:
            messagebox.showerror("Błąd", "Nie udało się pobrać ceny.")
            return
        self.assets.append({
            'symbol': symbol,
            'amount': amount,
            'price': price
        })
        self.calculate_total_value()

    def remove_asset(self, symbol):
        """Usuwa akcje z portfela."""
        self.assets = [asset for asset in self.assets if asset['symbol'] != symbol]
        self.calculate_total_value()

    def calculate_total_value(self):
        """Oblicza całkowitą wartość portfela."""
        self.total_value = sum(asset['amount'] * asset['price'] for asset in self.assets)

    def update_prices(self):
        """Aktualizuje ceny akcji w portfelu."""
        for asset in self.assets:
            asset['price'] = self.get_current_price(asset['symbol'])
        self.calculate_total_value()

    def predict_portfel_value(self, days):
        """Generuje prognozę wartości portfela na określoną liczbę dni."""
        total_value = self.total_value
        return list(map(lambda day: total_value * (1 + 0.001 * day), range(1, days + 1)))  # Konserwatywna prognoza 0.1% dziennie

    def optimize_portfel(self):
        """Analizuje i sugeruje optymalizację portfela."""
        if not self.assets:
            return ["Portfel jest pusty. Nie można przeprowadzić optymalizacji."]

        historical_data = {}
        for asset in self.assets:
            dates, prices = self.get_historical_data(asset['symbol'], limit=100)
            if not prices or len(prices) < 2:
                return [f"Brak wystarczających danych historycznych dla {asset['symbol']}."]
            historical_data[asset['symbol']] = prices

        if not historical_data:
            return ["Brak danych do optymalizacji."]

        # Optymalizacja Markowitza
        try:
            optimized_weights = self.markowitz_optimization(historical_data)
            if optimized_weights is not None:
                suggestions = self.generate_markowitz_suggestions(optimized_weights)
            else:
                suggestions = ["Nie można zoptymalizować portfela. Błąd podczas obliczeń."]
        except Exception as e:
            suggestions = [f"Nie można zoptymalizować portfela. Błąd: {e}"]

        return suggestions

    def markowitz_optimization(self, historical_data):
        """Optymalizacja Markowitza."""
        prices = np.array(list(historical_data.values()))
        returns = np.diff(prices, axis=1) / prices[:, :-1]
        mean_returns = np.array(list(map(np.mean, returns)))
        covariance_matrix = np.cov(returns)

        num_assets = len(self.assets)

        def portfel_variance(weights):
            return np.dot(weights.T, np.dot(covariance_matrix, weights))

        def neg_portfel_return(weights):
            return -np.dot(weights.T, mean_returns)

        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        bounds = tuple((0, 1) for _ in range(num_assets))
        initial_weights = np.array([1 / num_assets] * num_assets)

        optimized_result = minimize(
            neg_portfel_return,
            initial_weights,
            method='SLSQP',
            bounds=bounds,
            constraints=constraints
        )

        if optimized_result.success:
            return optimized_result.x
        else:
            return None

    def generate_markowitz_suggestions(self, optimized_weights):
        """Generuje sugestie na podstawie optymalizacji Markowitza."""
        suggestions = []
        for i, asset in enumerate(self.assets):
            current_weight = self.assets[i]['amount'] * self.assets[i]['price'] / self.total_value if self.total_value > 0 else 0
            optimized_weight = optimized_weights[i]
            difference = optimized_weight - current_weight
            if difference > 0.02:
                suggestions.append(
                    f"Zwiększ udział {asset['symbol']} do {optimized_weight * 100:.2f}% (z obecnych {current_weight * 100:.2f}%)."
                )
            elif difference < -0.02:
                suggestions.append(
                    f"Zmniejsz udział {asset['symbol']} do {optimized_weight * 100:.2f}% (z obecnych {current_weight * 100:.2f}%)."
                )
        if not suggestions:
            suggestions.append("Portfel jest zoptymalizowany zgodnie z modelem Markowitza.")
        return suggestions

    def get_current_price(self, symbol):
        """Pobiera aktualną cenę akcji z Finnhub."""
        try:
            quote = FINNHUB_CLIENT.quote(symbol)
            if quote and quote['c']:
                return quote['c']  # 'c' to aktualna cena
            else:
                messagebox.showerror("Błąd", f"Nie można pobrać ceny dla {symbol}.")
                return 0
        except Exception as e:
            messagebox.showerror("Błąd", f"Błąd API podczas pobierania ceny {symbol}: {e}")
            return 0

    def get_historical_data(self, symbol, limit=30):
        """Pobiera historyczne dane cenowe dla akcji z Finnhub."""
        try:
            today = datetime.date.today()
            from_date = today - datetime.timedelta(days=limit * 2)  # Dajemy zapas dni
            to_date = today
            res = FINNHUB_CLIENT.stock_candles(symbol, 'D', from_date.strftime('%Y-%m-%d'), to_date.strftime('%Y-%m-%d'))

            if res['s'] == 'ok':
                dates = [datetime.datetime.fromtimestamp(t) for t in res['t']]
                prices = res['c']  # Ceny zamknięcia
                return dates, prices
            else:
                messagebox.showerror("Błąd", f"Nie można pobrać danych historycznych dla {symbol}.")
                return [], []
        except Exception as e:
            messagebox.showerror("Błąd", f"Błąd API podczas pobierania danych historycznych {symbol}: {e}")
            return [], []
        
    @staticmethod
    def calculate_moving_average(prices, window=7):
        """Oblicza średnią ruchomą."""
        if len(prices) < window:
            return [np.nan] * len(prices)
        moving_average = np.convolve(prices, np.ones(window), 'valid') / window
        padding = [np.nan] * (window - 1)
        return padding + list(moving_average)


# ===============================
# Funkcje GUI
# ===============================
def create_gui(portfel):
    root = ThemedTk(theme="arc")
    root.title("Portfel Akcji")
    root.geometry("900x700")

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

    # Ramka do dodawania akcji
    frame_add = ttk.LabelFrame(scrollable_frame, text="Dodaj akcję do portfela", padding=10)
    frame_add.pack(fill="x", padx=10, pady=10)

    ttk.Label(frame_add, text="Symbol akcji:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    symbol_var = tk.StringVar()
    symbol_entry = ttk.Entry(frame_add, textvariable=symbol_var)
    symbol_entry.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(frame_add, text="Ilość:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
    amount_entry = ttk.Entry(frame_add)
    amount_entry.grid(row=1, column=1, padx=5, pady=5)

    def add_stock():
        symbol = symbol_var.get().upper()  # Symbol zawsze wielkimi literami
        amount = amount_entry.get()

        if not symbol or not amount:
            messagebox.showerror("Błąd", "Proszę uzupełnić wszystkie pola.")
            return

        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Ilość musi być większa od zera.")
            portfel.add_asset(symbol, amount)
            update_portfel_table()
            messagebox.showinfo("Sukces", f"Dodano {amount} {symbol} do portfela.")
        except Exception as e:
            messagebox.showerror("Błąd", str(e))

    ttk.Button(frame_add, text="Dodaj do portfela", command=add_stock).grid(row=2, column=0, columnspan=2, pady=10)

    # Ramka portfela
    frame_portfel = ttk.LabelFrame(scrollable_frame, text="Twój portfel", padding=10)
    frame_portfel.pack(fill="both", expand=True, padx=10, pady=10)

    columns = ("symbol", "amount", "price", "value")
    portfel_table = ttk.Treeview(frame_portfel, columns=columns, show="headings", height=10)
    for col in columns:
        portfel_table.heading(col, text=col.capitalize())
        portfel_table.column(col, anchor="center")
    portfel_table.pack(fill="both", expand=True)

    def remove_selected_stock():
        selected_item = portfel_table.selection()
        if not selected_item:
            messagebox.showerror("Błąd", "Proszę wybrać akcję do usunięcia.")
            return

        symbol = portfel_table.item(selected_item, 'values')[0]
        portfel.remove_asset(symbol)
        update_portfel_table()
        messagebox.showinfo("Sukces", f"Usunięto {symbol} z portfela.")

    ttk.Button(frame_portfel, text="Usuń wybraną akcję", command=remove_selected_stock).pack(pady=5)

    total_value_label = ttk.Label(frame_portfel, text="Wartość portfela: 0 USD")
    total_value_label.pack()

    def update_portfel_table():
        for row in portfel_table.get_children():
            portfel_table.delete(row)
        for asset in portfel.assets:
            portfel_table.insert("", "end", values=(
                asset['symbol'],
                asset['amount'],
                asset['price'],
                asset['amount'] * asset['price']
            ))
        total_value_label.config(text=f"Wartość portfela: {portfel.total_value:.2f} USD")

    # Ramka wykresu
    frame_chart_container = ttk.Frame(scrollable_frame)
    frame_chart_container.pack(fill="both", expand=True, padx=10, pady=10)

    frame_chart = ttk.Frame(frame_chart_container)
    frame_chart.pack(side="top", fill="both", expand=True, padx=10, pady=10)

    def update_chart():
        symbol = symbol_var.get().upper() # Pobierz symbol z pola tekstowego
        if not symbol:
            messagebox.showerror("Błąd", "Proszę wpisać symbol akcji.")
            return

        # Definicja globalnego selektora, aby był widoczny w calej funkcji update_chart
        global span_selector

        def fetch_data_and_update_chart():
            dates, prices = portfel.get_historical_data(symbol, limit=30)

            if not prices:
                messagebox.showerror("Błąd", "Nie udało się pobrać danych historycznych.")
                return
            if not dates:
                messagebox.showerror("Błąd", "Nie udało się pobrać dat historycznych.")
                return

            figure = Figure(figsize=(8, 6), dpi=100)
            ax = figure.add_subplot(111)

            ax.plot(dates, prices, label="Cena", color="skyblue")

            moving_average = portfel.calculate_moving_average(prices)
            ax.plot(dates, moving_average, label=f"SMA 7", color="darkred", linestyle='--')

            # Prognoza cen nie jest dostępna w darmowym planie Finnhub
            # predicted_mean, conf_int = portfel.forecast_prices(prices, days=7)

            # if predicted_mean is not None and conf_int is not None:
            #     forecast_days = [dates[-1] + datetime.timedelta(days=i + 1) for i in range(len(predicted_mean))]
            #     ax.plot(forecast_days, predicted_mean, label="Prognoza", linestyle="--", color='grey')

            #     # wyliczne przedziały ufność / wygenerowne zakres z lini prognozowania - i renderuje je pod grafe
            #     ax.fill_between(
            #         forecast_days,
            #         conf_int[:, 0],
            #         conf_int[:, 1],
            #         color="cornflowerblue",  # Zmiana koloru na intensywny niebieski
            #         alpha=0.4,  # delikatnie mniejsza transparentność
            #         label="Przedział ufności",
            #     )

            # ustawinia wykres / opis  grafu - i opisanych  elementów osi x/y

            ax.set_title(f"Cena {symbol}")
            ax.set_xlabel("Data")
            ax.set_ylabel("Cena [USD]")

            ax.legend()
            ax.grid(True)
            figure.autofmt_xdate()
            # zerowanie - widok - w widocznego w `Frame` (nie wywoal z Frame container tylko wykresy)
            for widget in frame_chart.winfo_children():
                widget.destroy()

            canvas_plot = FigureCanvasTkAgg(figure, frame_chart)
            canvas_plot.get_tk_widget().pack(fill="both", expand=True)
            canvas_plot.draw()

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
                canvas_plot.draw()

            span_selector = SpanSelector(
                ax, onselect, "horizontal", useblit=True)

        thread = threading.Thread(target=fetch_data_and_update_chart)
        thread.start()

    frame_buttons = ttk.Frame(
        frame_chart_container)  # umieszcze przyciski / do grafu poniżej wyliczonej ramki / kontenerem .
    frame_buttons.pack(side="bottom", fill='x', padx=10, pady=10)

    ttk.Button(frame_buttons, text="Aktualizuj wykres", command=update_chart).pack(side="left", pady=10)

    def clear_chart():  # by zerowało cała  strukture canvas
        for widget in frame_chart.winfo_children():
            widget.destroy()

    ttk.Button(frame_buttons, text="Wyczyść wykres", command=clear_chart).pack(side="right", pady=10)
    # Ramka prognoz wartości portfela
    frame_predictions = ttk.LabelFrame(scrollable_frame, text="Prognoza wartości portfela", padding=10)
    frame_predictions.pack(fill="both", expand=True, padx=10, pady=10)

    predictions_table = ttk.Treeview(frame_predictions, columns=("days", "value"), show="headings", height=3)
    predictions_table.heading("days", text="Dni")
    predictions_table.heading("value", text="Wartość (USD)")
    predictions_table.column("days", anchor="center")
    predictions_table.column("value", anchor="center")
    predictions_table.pack(fill="both", expand=True)

    def update_predictions_table():
        for row in predictions_table.get_children():
            predictions_table.delete(row)

        def fetch_predictions():
            predicted_values = portfel.predict_portfel_value(days=30)
            if predicted_values:
                for i, days in enumerate([1, 7, 30]):
                    if len(predicted_values) > i:
                        predictions_table.insert("", "end", values=(days, f"{predicted_values[i]:.2f}"))

        thread = threading.Thread(target=fetch_predictions)
        thread.start()

    ttk.Button(frame_predictions, text="Aktualizuj prognozy", command=update_predictions_table).pack(pady=10)

    # Ramka optymalizacji portfela
    frame_optimization = ttk.LabelFrame(scrollable_frame, text="Optymalizacja portfela", padding=10)
    frame_optimization.pack(fill="both", expand=True, padx=10, pady=10)

    optimization_text = tk.Text(frame_optimization, height=5, wrap="word")
    optimization_text.pack(fill="both", expand=True)

    def update_optimization():
        def fetch_suggestions():
            suggestions = portfel.optimize_portfel()
            optimization_text.delete("1.0", tk.END)
            if suggestions:
                optimization_text.insert(tk.END, "\n".join(suggestions))
            else:
                optimization_text.insert(tk.END, "Portfel jest zoptymalizowany.")

        thread = threading.Thread(target=fetch_suggestions)
        thread.start()

    ttk.Button(frame_optimization, text="Zaktualizuj optymalizację", command=update_optimization).pack(pady=10)

    # Inicjalizacja danych
    update_portfel_table()
    update_predictions_table()
    update_optimization()

    root.mainloop()


# ===============================
# Główna funkcja aplikacji
# ===============================
def main():
    """Uruchamia aplikację Portfel akcji."""
    portfel = Portfel()
    create_gui(portfel)

if __name__ == "__main__":
    main()