# pip install 
import pandas as pd

dane=pd.read_csv('ścierzka\\do\\pliku.csv')#odczyt
dane.to_csv('ścierzka\\gdzie\\stworzy\\plik.csv') #po przecinku po ścierzce sep=";", dtype=()
#dane jeest słownikem
dane = pd.DataFrame(dane)#robi dataframe(ładnie wyglądający słownik) z słownika 
dane.head() #5 pierwszych rekordów

dane['nazwaKolumny']
dane[2:3] #kolumny od 2 do 3

dane.nazwaKolumny.unique()#da unikalne wartości danych z kolumny, return counts jest spoko

dane.shape #pokarze wielkość tablicy
dane.info()#da informacje na temat dataframe
dane.nazwakolumny.describe() #do całego albo do kolumny opisuje, liczbe rek, średnią, std ,min ,kwantyle ,max zwracana w data frame chyba

dane.loc['indexw6721','kolumna']#pokarzy jaka jest wartość dla tego indeksu musi się zawsze rużnić i nie powtarzać

#iteracja po wierszach 
for index,row in dane.iterrows():
    row['osoba']#wypisze wyszystkie wartości w osobie
    if row["osoba"]=="jan":
        print(row)#iteruje po wierszach a jak dojdzie do dobrego wypisuje jego zawartość

print(dane[dane['osoba']=="jan"]) | (dane['ur']<2000)#poda nam osobe jan i ur <2000

#modyfikacja danych
dane["wiek"]= 2022-dane['ur']#dodaje kolumne wiek

dane.drop('ur',axis=1,inplace=True)#usuwa kolumne urodzenia

#scalanie kolumn
dane['imie_nazwisko']=dane['imie']+' '+dane['nazwisko']
dane.drop('imie',axis=1,inplace=True)
dane.drop('nazwisko',axis=1,inplace=True)

#rozdzielanie 
dane[['first','sec']]=dane.imie_nazwisko.str.split(' ',expand=True)

#grupowanie 
wynik=dane.groupby('rok').count() #liczy ile jest rekordów po wartośći roku

wynik=dane.groupby('rok').mean()
#da się gorsze monstra robić ale nie chce mi się 

#funkcje
def funkcja():
    pass
#masz funkcje coś robiącą 
dane.punkty.apply(funkcja)#punkty to nazwa kolumny
df1,df2=0
#jeśli dataframe ma takie same wartości
x=pd.concat([df1,df2])

x=pd.merge(df1,df2, on='nazwisko', how='inner')

#łączenie do SQL
import sqlite3 as sql

connection = sql.Connection('myDB')
connection.execute('''KOMENDA SQL   ''')
sql=connection.execute('''KOMENDA SQL Select''')
df=pd.DataFrame(sql)
connection.close()
print(df)
i=0
lista=[]
lista.remove(20) #usuwa podaną wartosć 
lista.append(20)#dodaje podaną wartość
lista.insert(i, x)#  wstawia x przed indeksem i; .
lista.count(x)  #zwraca ilość wystąpień x; .
lista.index(x)  #zwraca indeks pierwszego wystąpienia x; 
lista.pop()  #usuwa i zwraca ostatni element listy;
lista.reverse()# odwraca porządek w liście
reversed(lista)# zwraca kopię listy w odwróconym porządku;
lista.sort()  #sortuje listę 
lista.sort(reverse = False/True)# sortuje listę malejąco/rosnąco
sorted(lista) #zwraca kopię listy posortowanej rosnąco;

#krotka () uporzątkowany ciąg
krotka=1,2,3
lista.extend(krotka)

#sety { } 
# add dodawanie wartości
#remove usuwa jak nie ma błąd
#discart usuwa jak nie ma idzie dalej
#cler czyści 
#del usuwa zbiór
#zbiór.ubdate - dodaje element do zbioru
# set1.intersection(set2) - część wspólna
# s1.union(s2) – suma zbiorów
# s1.issubset(s2) – sprawdzenie czy s1 jest podzbiorem s2
# s1.isdisjoint(s2) – sprawdzenie czy s1, s2 są rozłączne


#wyk 6 zapisywanie do pliku i doczyt
#wyk 7 klasy
#wyk 8 dziedziczenie
import seaborn as sns
#mam nadzieje ze będę mógł mieć wykresy podebrane z moodle wykl 9
import os

import numpy as np

import matplotlib.pyplot as plt

#ez wykres liniowy bardzo podstawowy bez punktów 
plt.plot([1, 2, 3, 4])
plt.ylabel('jakieś liczby')
plt.show()

# wartości, najpierw dla wektora x, y
# parametr w postaci stringa,określa styl wykresu
#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro-')
# lista parametrów w postaci [xmin, xmax, ymin, ymax]
plt.axis([0, 6, 0, 20])
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 5, 0.2)

# wygenerować wiele wykresów na jednym "płótnie" (ang. canvas
# podając niezbędne wartości: wartości dla osi x, wartości dla osi y, styl wykresu, ...
plt.plot(x, x, 'r--', x, x**2, 'bs', x, x**4, 'g^')
plt.show()


import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2, 100)
# wykresy mogą być też dodawane do płótna definicja po definicji zamiast w pojedynczym wywołaniu funkcji plot()
# tutaj też mam parametr label, który określa nazwę danego wykresu w legendzie
plt.plot(x, x, label='liniowa')
plt.plot(x, x**2, label='kwadratowa')
plt.plot(x, x**3, label='sześcienna')
# etykiety osi i nazwa
plt.xlabel('etykieta x')
plt.ylabel('etykieta y')
plt.title("Prosty wykres")
#pokarze legende
plt.legend()
plt.show()


#to samo co wyrzej tylko przyjmujemy sinusa
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 10, 0.1)
s = np.sin(x)
plt.plot(x, s, label='sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title("Wykres sin(x)")
plt.legend()
plt.show()

#scater plot z R
import matplotlib.pyplot as plt
import numpy as np
# dane w formie słownika, ale równie dobrze może to być Pandas DataFrame
data = {'a': np.arange(50),
 'c': np.random.randint(0, 50, 50),
 'd': np.random.randn(50)}

data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

# aby w ten sposób przekazać parametry wykresu należy dodać niezbędny 
# parametr data, który zawiera dane dostępne poprzez etykiety
# to oznacza, że 'a' jest równoważne data['a'] itd. Parametr c to skrót od 
# color, tutaj przekazywany w formie wektora
# wartości kolorów dla każdej kolejnej wartości wykresu. Parametr s to 
# scale - określa rozmiar, w tym przypadku punktu, dla
# każdej kolejnej wartości wektora wykresu. Reasumując dla pierwszego 
# punktu wykresu będą brane poniższe wartości
print(f"a={data['a'][0]}, b={data['b'][0]}, c={data['c'][0]}, 
d={data['d'][0]}")
plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('wartość a')
plt.ylabel('wartość b')
plt.show()

#potem robi wiele wykresów jako jeden wynik ale to chyba za dużo 

#prosty wykres słupkowy
import numpy as np
import matplotlib.pyplot as plt
etykiety = ['K', 'M']
wartosci = [345, 435]
plt.bar(etykiety, wartosci)
plt.ylabel('Ilość narodzin')
plt.xlabel('Płeć')
plt.show()



#wykres kołowy mało przydatny ale ładnie wygląda
zawodnicy = ['Messi', 'Suarez', 'Dembele', 'Coutinho']
bramki = [48, 25, 13, 11]
def prepare_label(pct, br):
 absolute = int(pct / 100. * np.sum(br))
 return "{:.1f}%".format(pct, absolute)
wedges, texts, autotexts = plt.pie(bramki, labels=zawodnicy,
 autopct=lambda pct: prepare_label(pct, 
bramki), textprops=dict(color="black"))
plt.setp(autotexts, size=14, weight="bold")
plt.legend(title='Zawodnicy')
plt.show()

#potem rob i zaawanwsowane tutorial pod linkiem
# https://towardsdatascience.com/matplotlib-tutorial-learn-basics-of-pythons-powerful-plotting-library-b5d1b8f67596


#rozkład prawdopodobieństwa
import numpy as np
import matplotlib.pyplot as plt
x = np.random.randn(10000)
# bins oznacza ilość "koszy" czyli słupków, do których mają wpadać wartości z wektora x
# facekolor oznacza kolor słupków
# alpha to stopień przezroczystości wykresu
# density oznacza czy suma ilości zostanie znormalizowana do rozkładu prawdopodobieństwa (czyli przedział 0, 1)
plt.hist(x, bins=50, facecolor='g', alpha=0.75, density=True)
plt.xlabel('Wartości')
plt.ylabel('Prawdopodobieństwo')
plt.title('Histogram')
# wyświatlanie siatki
plt.grid(True)
plt.show()