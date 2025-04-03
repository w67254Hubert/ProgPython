import requests

def search_symbols(api_key, keyword):
    #
    # Searches for stock symbols using the Alpha Vantage API.

    # Args:
    #     api_key: Your Alpha Vantage API key.
    #     keyword: The keyword to search for (e.g., company name).

    # Returns:
    #     A list of matching symbols and their details, or None if an error occurs.
    # 
    url = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={keyword}&apikey={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()

        if "bestMatches" in data:
            return data["bestMatches"]
        else:
            print(f"Error: No matching symbols found or API error: {data}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        return None

# Example usage:
api_key = ""  # Replace with your actual API key
keyword = "PKO"  # Example keyword
####asdad
wynik = search_symbols(api_key, keyword)

if wynik:
    for dopasowanie in wynik:
        print(f"Symbol: {dopasowanie['1. symbol']}")
        print(f"Name: {dopasowanie['2. name']}")
        print(f"Type: {dopasowanie['3. type']}")
        print(f"Region: {dopasowanie['4. region']}")
        print(f"Otwarcie rynku: {dopasowanie['5. marketOpen']}")
        print(f"Zamknięcie rynku: {dopasowanie['6. marketClose']}")
        print(f"strefa czasowa: {dopasowanie['7. timezone']}")
        print(f"waluta: {dopasowanie['8. currency']}")
        print("-" * 20)