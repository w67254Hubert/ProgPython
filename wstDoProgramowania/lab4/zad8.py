'''(8.py) Napisz skrypt, który wyświetli gwiazdki jak poniżej. Liczba wierszy (lub gwiazdek w linii)
powinna być podawana przez użytkownika.
Przykład: 3
* * *
* * *
* * *'''


x=int(input("podaj liczbe"))

for i in range(x):
    for i in range(x):
        print("*  ",end='  ')
    print()



