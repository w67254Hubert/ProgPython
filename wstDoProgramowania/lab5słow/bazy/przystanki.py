ulice =[
    # "Aleja_Lipowa", "ulica_Kwiatowa", "Plac_Słoneczny", "Skwer_Brzozowy", "ulica_Kasztanowa",
    # "Plac_Różany", "Aleja_Miodowa", "ulica_Jastrzębia", "Skwer_Klonowy", "ulica_Cedrowa",
    # "Plac_Akacjowy", "Aleja_Wiśniowa", "ulica_Topolowa", "Skwer_Dębowy", "ulica_Malinowa",
    # "Plac_Cynamonowy", "Aleja_Sosnowa", "ulica_Rozmarynowa", "Skwer_Orzechowy", "ulica_Jabłkowa",
    # "Plac_Lawendowy", "Aleja_Brzozowa", "ulica_Lipcowa", "Skwer_Makowy", "ulica_Bukowa", "Plac_Zielony",
    # "Aleja_Rozowa", "ulica_Bezowa", "Skwer_Lawendowy", "ulica_Cytrynowa", "Plac_Kwiatowy",
    # "Aleja_Miętowa", "ulica_Gruszkowa", "Skwer_Miodowy", "ulica_Jagodowa", "Plac_Żurawinowy",

    "Aleja_Czerwona", "ulica_Porzeczkowa", "Skwer_Borówkowy", "ulica_Ananasowa", "Plac_Brzoskwiniowy",
    "Aleja_Pomarańczowa", "ulica_Truskawkowa", "Skwer_Melonowy", "ulica_Granatowa", "Plac_Malinowy",
    "Aleja_Dyniowa", "ulica_Morelowa", "Skwer_Winogronowy", "ulica_Aroniowa", "Plac_Cytrynowy",
    "Aleja_Ananasowa", "ulica_Mango", "Skwer_Paprykowy", "ulica_Malinowy_Sad", "Plac_Pomidorowy",
    "Aleja_Porzeczkowa", "ulica_Wiśniowy_Sad", "Skwer_Brzoskwiniowy", "ulica_Jeżynowa", "Plac_Jabłkowy",
    "Aleja_Gruszkowa", "ulica_Arbuzowa", "Skwer_Truskawkowy", "ulica_Mango", "Plac_Mandarynkowy",
    "Aleja_Paprykowa", "ulica_Liczi", "Skwer_Kiwi", "ulica_Persymonowa", "Plac_Marakuja",
    "Aleja_Kaktusowa", "ulica_Guawa", "Skwer_Awokado", "ulica_Jagodowy_Sad", "Plac_Ananasowy",
    "Aleja_Marakui", "ulica_Kiwi", "Skwer_Malinowy_Sad", "ulica_Mandarynkowa", "Plac_Mango",
    "Aleja_Brzoskwiniowa", "ulica_Papaja", "Skwer_Grejpfrutowy", "ulica_Kiwi", "Plac_Winogronowy",
    "Aleja_Arbuza", "ulica_Jeżynowa", "Skwer_Malinowy", "ulica_Jabłkowy_Sad", "Plac_Kiwi",
    "Aleja_Truskawkowa", "ulica_Malinowa_Polana", "Skwer_Wiśniowy", "ulica_Kaktusowa", "Plac_Aroniowy",
    "Aleja_Grejpfrutowa", "ulica_Awokado", "Skwer_Liczi", "ulica_Malina"]
Miasto="Nibylandia"

import random

def generuj_liste_nieparzystych(ilosc_elementow):
    lista_nieparzystych = random.sample(range(1, 72, 2), min(ilosc_elementow, 36))
    return lista_nieparzystych

# Podaj ilość elementów w liście nieparzystych
ilosc_elementow = 37

# Wygeneruj i wyświetl listę nieparzystych
lista_nieparzystych = generuj_liste_nieparzystych(ilosc_elementow)
print(len(lista_nieparzystych))

i=63  #63 dla bez przys 35 dla z przys
while i>=0:
    print("('",ulice[i],"','",ulice[i],"_",Miasto,"',",1,"),") #lista_nieparzystych[i] lub 1
    i=i-1