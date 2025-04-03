import alpha_vantage.timeseries as av
import pandas as pd
from datetime import datetime

# Zastąp swoim kluczem API
API_KEY = ""

# Symbol akcji
SYMBOL = "IBM"
####asdad
def pobierz_dane_alpha_vantage(symbol, api_key):
    """Pobiera dane z Alpha Vantage dla danego symbolu."""
    try:
        ts = av.TimeSeries(key=api_key, output_format='pandas')
        data, meta_data = ts.get_daily(symbol=symbol, outputsize='full') # 'compact' - ostatnie 100 dni, 'full' - cała historia
        return data, meta_data
    except Exception as e:
        print(f"Błąd podczas pobierania danych dla {symbol}: {e}")
        return None, None

def filtruj_dane_z_miesiąca(data):
    """Filtruje dane, aby zawierały tylko dane z bieżącego miesiąca."""
    now = datetime.now()
    bieżący_rok = now.year
    bieżący_miesiąc = now.month

    # Filtruj dane
    data_z_miesiąca = data[(data.index.year == bieżący_rok) & (data.index.month == bieżący_miesiąc)]
    return data_z_miesiąca


if __name__ == "__main__":
    dane, meta_dane = pobierz_dane_alpha_vantage(SYMBOL, API_KEY)

    if dane is not None:
        dane_z_miesiąca = filtruj_dane_z_miesiąca(dane)

        if not dane_z_miesiąca.empty:
            print("Dane z bieżącego miesiąca dla IBM:")
            print(dane_z_miesiąca)

            # Przykład: Oblicz średnią cenę zamknięcia
            srednia_cena = dane_z_miesiąca['4. close'].mean()
            print(f"\nŚrednia cena zamknięcia w tym miesiącu: {srednia_cena:.2f}")

            # Przykład: Wyświetl meta dane (informacje o pobranych danych)
            print("\nMeta Data:")
            print(meta_dane)
        else:
            print("Brak danych dla IBM w tym miesiącu.")
    else:
        print("Nie udało się pobrać danych dla IBM.")