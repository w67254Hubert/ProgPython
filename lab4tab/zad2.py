'''Zadanie 2.
• Utwórz listę zestaw_1 zawierającą liczby losowe z przedziału [1, 10]. Liczbę elementów listy podaje
użytkownik. Wyświetl listę.
• Utwórz drugą listę zestaw_2 zawierającą liczby losowe z przedziału [5, 15]. Liczbę elementów listy
podaje użytkownik. Wyświetl listę.
• Pobierz od użytkownika liczbę. Napisz instrukcję warunkową, która na podstawie wartości
zapisanych w listach wyświetli jeden z poniższych komunikatów: „Liczba z zestawu 1”, „Liczba z
zestawu 2” albo „Nie ma takiej liczby w obu zestawach”.
• Utwórz listę zestaw_1_2 będącą złączeniem wartości z list zestaw_1 oraz zestaw_2. Posortuj i wyświetl
listę'''
import random
zestaw_1 = []
n = int(input("Podaj rozmiar lista: "))
for i in range(n):
    x = random.randint(1, 10)
    zestaw_1.append(x)
    print(zestaw_1)

n = int(input("Podaj rozmiar lista: "))
zestaw_2 = [random.randint(5, 15) for i in range(n)]
print(zestaw_2)

