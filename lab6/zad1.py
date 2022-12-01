'''Napisz funkcję o dwóch parametrach, imię oraz wiek, która wypisze ich wartości na ekranie.
• Dodaj w następnej linii po nagłówku funkcji komentarz opisujący działanie funkcji. Wyświetl ten opis za
pomocą instrukcji
print(nazwa_funkcji.__doc__)
• Jeśli w wywołaniu funkcji nie podano wieku, przypisz do parametru wiek wartość domyślną 20.
Uwaga: Parametry z wartościami domyślnymi powinny być definiowane jako ostatnie na liście
parametrów, ponieważ Python dopasowuje argumenty do parametrów na podstawie ich pozycji:
def fun(param1, param2=default2, param3=default3)'''

# def z1(imie,wiek):
#     '''Funkcja wypisuje imie oraz wiek.
#
#     :param imie:
#     :param wiek:
#     :return:
#      '''
#
#
#
#     print(imie,wiek)
#
# z1("karolina",21)
# z1("michał",32)
# z1(wiek=23,imie="karolina")
#
# print(z1.__doc__)
#
# print(help(z1))

def z1(imie,wiek=20):
    ''' Funkcja wypisuje imie oraz wiek.

    :param imie:
    :param wiek:
    :return:

    '''
    print(imie,wiek)

z1("Karolina",21)
z1("Michał",32)
z1(wiek=23,imie="Karolina")
print(z1.__doc__)
print(help(z1))
z1("Karolina")