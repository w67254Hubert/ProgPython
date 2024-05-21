import random

# Będzie 36 autobusów
i = 36

# Lista do przechowywania stanów
Stan = ["'aktywny'", "'nieaktywny'"]

# Ustalanie wag dla stanów
wagi = [0.8, 0.2]  # Dla 'aktywny' - 0.8, dla 'nieaktywny' - 0.2

# Losowe wypełnienie tabeli i uwzględnienie wag
lisstan = [random.choices(Stan, weights=wagi)[0] for _ in range(i)]

# Wyświetlenie wyniku
print(len(lisstan))

marmod = ["'Volvo 7000'", "'Mercedes Conecto LF'", "'Mercedes Conecto LF G'", "'Solaris Urbino 10 III'", "'Solaris Urbino 12 III'", "'MAN NG313 Lion’s City G CNG'", "'MAN NG363 Lion’s City G'", "'MAN NL313 Lion’s City CNG'"]
miejsca = [70, 166, 81, 104, 175, 175, 100]
marmod2 = []
miejsca2 = []

e=7
while e>=0:
    i = 6
    while i >= 0:
        tym1 = marmod[i]
        tym2 = miejsca[i]
        marmod2.append(tym1)
        miejsca2.append(tym2)
        i = i - 1
    e=e-1
print("marmod2:", len(marmod2))
print("miejsca2:", len(miejsca2))

import random
import string

def generuj_rejestracje():
    poczatek_rejestracji = "RZ"
    losowe_znaki = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    rejestracja = poczatek_rejestracji + losowe_znaki
    return rejestracja

# Wygeneruj i wyświetl losową rejestrację
rejestracja = generuj_rejestracje()
import random

def generuj_liste_parzystych(ilosc_elementow):
    lista_parzystych = random.sample(range(2, 73, 2), min(ilosc_elementow, 36))
    return lista_parzystych

# Podaj ilość elementów w liście parzystych
ilosc_elementow = 37

# Wygeneruj i wyświetl listę parzystych
lista_parzystych = generuj_liste_parzystych(ilosc_elementow)
# print(lista_parzystych)
print(len(lista_parzystych))

i=35
while i>=0:
    rej=generuj_rejestracje()
    print("(",lisstan[i],",",marmod2[i],",",miejsca2[i],",'",rej,"',",lista_parzystych[i],"),")
    i=i-1
