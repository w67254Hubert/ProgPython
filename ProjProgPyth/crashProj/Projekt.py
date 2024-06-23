# Dobrze przygotowany projekt powinien mieć:
# - zaczyt/odczyt danych z pliku (JSON, CSV, inne) lub urządzenia 
# - przetwarzanie danych 
# - wykresy/analiza danych Opis projektu:
# 0. Strona tytułowa 
# 1. Opis produktu 
# 2. Schematy akcji lub przypadków użycia 
# 3. Prezentacja systemu 
# 4. Bibliografia Styl zgodny ze stylem pracy inż. 
# Ocena składa się z: 
# - oceny działającego programu (prezentowanego po dowolnym laboratorium lub na ostatnich zajęciach projektowych) 
# UWAGA. Można pracować w zespołach dwuosobowych. W takich przypadkach wszyscy autorzy zamieszczają komplet plików na moodlu.
# Brak plików oznacza ocenę niedostateczną. Proszę prac nie wysyłać na maila.

#https://www.kaggle.com/datasets/jacksondivakarr/car-crash-dataset/data
#Wczytywanie, analiza i wizualizacja danych wypadków samochodowych. język Python

import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
import seaborn as sns

class przetwarzanie:
    #wczytaj csv i utwurz plik do zapisu
    def __init__(self,data=None):
            self.data=data    
    def getdata(self):
         return self.data
    def setdata(self,data):
         self.data=data

    def info(self):
         #sprawdzenie podanego obiektu
        missing_values = data.isnull().sum()
        data_types = data.dtypes
        print("ilość NA wartoći w dataframe \n",missing_values)
        print("typy danch w dataframe \n", data_types)

    #1 co spowodowało wypadki
    def IleWypadkow(self):
        factor=data['Primary_Factor']
        factorNP=factor.to_numpy()
        # print(np.unique(factorNP))
        wartosc,ilosc=np.unique(factorNP,return_counts=True)

        filtr_indices = ilosc >= 20 #ucinanie przypadków "pojedyńczych" by mniejszyć wykres
        wartosc = wartosc[filtr_indices]
        ilosc = ilosc[filtr_indices]

        plt.figure(figsize=(10, 6))
        plt.bar(wartosc, ilosc)
        plt.ylabel('Ilość przypadków')
        plt.xlabel('Typ wypadku drogowego')
        plt.title('Liczba wypadków drogowych według typu')
        plt.xticks(rotation=45, ha='right')#można
    #   plt.savefig('test.jpg')
        plt.show()

        i=0
        wszyskie=sum(ilosc)
        for x in ilosc:
            proc=(x/wszyskie)*100#peocenty
            if round(proc, 2)<0.01:
                print(wartosc[i],"wystąpiła",ilosc[i],"a to poniżej 0,1% wypadków!!")

            else:
                print(wartosc[i],"wystąpił",ilosc[i],"a to",round(proc, 2),"% wypadków")
            i+=1
        #I to np do tablicy albo zapisać w csv.


    def ileAutWyp(self):
         #2 jaki procent wypadków miały wypadki zawierające więcej niż 3 samochody
        #wykres słupokowy ilości wypadków w zależności od pojazdów uszkodzonych w wypadku?
        factor=data['Collision_Type']
        factorNP=factor.to_numpy()
        # print(np.unique(factorNP))
        wartosc,ilosc=np.unique(factorNP,return_counts=True)

        plt.figure(figsize=(10, 6))
        plt.bar(wartosc, ilosc)
        plt.ylabel('Ilość przypadków')
        plt.xlabel('rodzaj uczestnika ruchu w wypadku')
        plt.title('Liczba uczestników ruchu biorących udział w wypadku')
        plt.xticks(rotation=45, ha='right')#można
        #   plt.savefig('test.jpg')

        plt.show()

        wszyskie=sum(ilosc)
        i=0
        for x in ilosc:
                proc=(x/wszyskie)*100
                if round(proc, 2)<1:
                    print(wartosc[i],"wystąpiła",ilosc[i],"a to poniżej 1% wypadków")
                    
                else:
                    print(wartosc[i],"wystąpił",ilosc[i],"a to",round(proc, 2),"% wypadków")
                i+=1
    def obrazenia(self):
        #4 ile jest/jaki procent rekordów tworzą z znanym uszkodzeniem ciała injury/unknown
        factor=data['Injury_Type']
        factorNP=factor.to_numpy()
        # print(np.unique(factorNP))
        wartosc,ilosc=np.unique(factorNP,return_counts=True)

        plt.figure(figsize=(10, 6))
        plt.bar(wartosc, ilosc)
        plt.ylabel('procętowy rozkład przypadków')
        plt.xlabel('typ obrarzeń')
        plt.title('Podział procentowy przypadków obrażeń')
        plt.xticks(rotation=0, ha='right')
        #   plt.savefig('test.jpg')
        plt.show()
        #może dodać to do csv czy coś
        wszyskie=sum(ilosc)
        i=0
        for x in ilosc:
                proc=(x/wszyskie)*100
                if round(proc, 2)<1:
                    print(wartosc[i],"wystąpiła",ilosc[i],"a to poniżej 1%","brażeń")
                    
                else:
                    print(wartosc[i],"wystąpił",ilosc[i],"a to",round(proc, 2),"%", "obrażeń")
                i+=1
    def Weekend(self):
        #5 kiedy zdarza się więcej wypadków na dzień w dnie pracy czy weekendy?
        factor=data['Weekend?']
        factorNP=factor.to_numpy()
        wartosc,ilosc=np.unique(factorNP,return_counts=True)

        ProcIlosci=[] 
        wszyskie=sum(ilosc)
        i=0
        for x in ilosc:
            proc=(x/wszyskie)*100
            ProcIlosci.append(proc)

        plt.figure(figsize=(10, 6))
        plt.bar(wartosc, ProcIlosci)
        plt.ylabel('procętowy rozkład przypadków')
        plt.xlabel('typ obrarzeń')
        plt.title('Podział procentowy przypadków obrażeń')
        plt.xticks(rotation=0, ha='right')
        #   plt.savefig('test.jpg')
        plt.show()
        wszyskie=sum(ilosc)
        i=0
        for x in ilosc:
                proc=(x/wszyskie)*100
                print(wartosc[i],"było",ilosc[i],"wypadków, a to",round(proc, 2),"% wypadków w danych")
                i+=1

    def wypGldzin(self):
    #6 w jakich godzinach dochodzi do największej liczby wypadków albo wykres liniowy z godzinammi ilością wypadków podczas nich. (napraw te godziny)
    #godzin nie przerabiaj tylko podziel je przez 100 i będize wyglądac nadal dobrze bo potrzebujesz tylko kolejności

        factor=data['Hour']
        factorNP=factor.to_numpy()
        wartosc,ilosc=np.unique(factorNP,return_counts=True)
        wartosc=wartosc/100 #poniewarz z jakiegoś popwodu wareości godzinowe są w dziwnym formacie

        plt.figure(figsize=(10, 6))
        plt.plot(wartosc, ilosc, marker='o', linestyle='-', color='b')
        plt.ylabel('Procentowy rozkład przypadków')
        plt.xlabel('Godzina')
        plt.title('Podział przypadków obrażeń')
        plt.xticks(rotation=0, ha='right')
        plt.grid(True)
        plt.show()


#7 bedziesz miec godziny wypadkow np to predykcje mozesz zrobic np ze od godzin 0-4 najczesciej jest distracted kierowca
##zapis do csv
# path = 'C:\\Users\\hubla\\Documents\\studia-pliki\\repozytoria\\ProgPython\\ProjProgPyth\\crashProj\\wynik.csv'
# if os.path.exists(path):
#     data2 = pd.read_csv(path)
# else:
#     print("File does not exist. Creating a new file.")
#     # Tworzymy przykładowy DataFrame
#     data2 = pd.DataFrame({
#         'Brand': ['Toyota', 'Ford', 'BMW'],
#         'Model': ['Corolla', 'Mustang', 'X5'],
#         'Year': [2020, 2019, 2018]
#     })
#     # Zapisujemy DataFrame do pliku Excel
#     data2.to_csv(path, index=False)


#do klasy prostego menu konsolowego
def clear_terminal(): #czysczenie terminala po wykoaniu danego kodu

        os.system('cls')

#pobieranie csv
path = 'C:\\Users\\hubla\\Documents\\studia-pliki\\repozytoria\\ProgPython\\ProjProgPyth\\crashProj\\car.csv'
if os.path.exists(path):          
    data = pd.read_csv(path,dtype={
    'Year': 'Int64',
    'Month': 'Int64',
    'Day': 'Int64',
    'Weekend?':pd.StringDtype(),
    'Hour':'Int64',
    'Collision_Type':pd.StringDtype(),
    'Injury_Type':pd.StringDtype(),
    'Primary_Factor':pd.StringDtype(),
    'Reported_Location':pd.StringDtype(),
    'Latitude':'float',
    'Longitude':'float',
    })
    print("DataFrame loaded from CSV file.")
    data = pd.DataFrame(data)
    data.dropna(inplace=True)#wywaliłem na bo psuły kod
else:
    print("File do not exists")
    
przet=przetwarzanie(data)
#print(przet.getdata())
przet.info()
przet.obrazenia()
muszisz udoskolalić opisy wszystkiego i pewnie wypisy w rzeczach dodaj jako listy/słowniki do pobrania

# csv.info()

#input("klik by kontynuować")
#clear_terminal()



    #zapisz odpowiedzi na pytania w pliku



