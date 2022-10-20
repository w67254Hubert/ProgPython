'''Zadanie 1 (1.py):
• Dla osób poniżej 4 roku życia wstęp jest bezpłatny.
• Dla osób w wieku od 4 do 18 lat bilet kosztuje 10zł.
• Dla osób powyżej 18 roku życia bilet kosztuje 20zł.
Przykład: Wprowadź wiek klienta: 5
Cena biletu: 10zł'''

a = (int)(input("Proszę podać wiek klienta: "))
if a<4:
    print("Wstęp jest bezpłatny")
elif a<=18:
    print("Cena biletu: 10zł")
else:
    print("Cena biletu kosztuje 20zł")
