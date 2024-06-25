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
import matplotlib.pyplot as plt
#mam nadzieje ze będę mógł mieć wykresy podebrane z moodle wykl 9
import os

import numpy as np

