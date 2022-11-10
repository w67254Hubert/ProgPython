'''Zadanie 5. Utwórz listę punkty będącą listą punktów zdobytych z pewnego egzaminu przez grupę 15 studentów.
Punkty niech będą liczbami rzeczywistymi z przedziału [0; 50]. Następnie
• Wyświetl informację o największej i najmniejszej ilości zdobytych punktów
• Wyświetl indeks pierwszego wystąpienia punktów podanych przez użytkownika. Jeżeli taka liczba
punktów nie występuje na liście, wyświetl odpowiedni komunikat
• Oblicz średnią punktów liczbę punktów z egzaminu
• Oblicz, ile osób zdobyło punkty powyżej, a ile poniżej średniej
• Wyświetl punkty poniżej średniej
• Wyświetl punkty powyżej średniej
'''
import random
punkty=[]
ponizej=[]
for x in range(15):
    punkty.append(round(random.uniform(0,50),2))
print(punkty)
print(f" wartość minimalna: {min(punkty)}")
print(f" wartość maksymalna: {max(punkty)}")
liczba = float(input("Podaj liczbe: "))
if liczba in punkty:
    print(punkty.index(liczba))
else:
    print('nie ma takiej liczby')
suma= sum(punkty)
srednia=round(suma/len(punkty),2)
print(f"srednia ilosc punktow: {srednia}")
for y in punkty:
    if y < srednia:
        ponizej.append(y)
powyzej=[y for y in  punkty if y > srednia]
print(f"osoby ponizej sredniej {ponizej}, osoby powyzej sredniej {powyzej}")
print(len(ponizej), len(powyzej))