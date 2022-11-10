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