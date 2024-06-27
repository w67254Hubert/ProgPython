
#  Dobrze przygotowany projekt powinien mieć:
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
import seaborn as sns#dalej nie urzyte

class przetwarzanie:
    #wczytaj csv i utwurz plik do zapisu
    def __init__(self,data=None):
            self.data=data    
    def getdata(self):
         return self.data
    def setdata(self,data):
         self.data=data

    def info(self):
        data=self.data
         #sprawdzenie podanego obiektu
        missing_values = data.isnull().sum()
        data_types = data.dtypes
        print("ilość NA wartoći w dataframe \n",missing_values)
        print("typy danch w dataframe \n", data_types)
   
    def IleWypTyp(self):  #1 co spowodowało wypadki i ile tego jest
        data=self.data
        factor=data['Primary_Factor']#wybieram kolumne
        factorNP=factor.to_numpy()
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
    #   plt.savefig('test.jpg') jest tak bo nie chce zapisywać za karzdym razem jak wyświetlam wykres
        plt.show()

        print("Podsumowanie wykresu")
        procenty=[]
        wszyskie=sum(ilosc)
        for x in ilosc:
            proc=(x/wszyskie)*100#peocenty
            procenty.append(round(proc,2))

        wynik = dict({
             "Typ Wypadku": wartosc ,
                "ile": ilosc,
                "Udział%":procenty })
        wynik=pd.DataFrame(wynik)
        print(wynik)
        odp=str(input("czy chcesz zapisać wynik? T/N "))
        if odp.upper()=="T":
            zapDoCSV(wynik)
        else: print("Anulowano zapis") 

        #return(wynik) #poda nam dataframe który potem będziemy mogli zapisać albo odczytać
            #szybko morzna to zapisać


    def ileAutWyp(self):
        data=self.data
         #2 jaki procent wypadków miały wypadki zawierające więcej niż 3 samochody
        #wykres słupokowy ilości wypadków w zależności od pojazdów uszkodzonych w wypadku?
        factor=data['Collision_Type']
        factorNP=factor.to_numpy()
        # print(np.unique(factorNP))
        wartosc,ilosc=np.unique(factorNP,return_counts=True)

        plt.figure(figsize=(10, 6))
        plt.bar(wartosc, ilosc)
        plt.ylabel('Ilość przypadków')
        plt.xlabel('Typ uczestnika ruchu w wypadku')
        plt.title('Liczba uczestników ruchu biorących udział w wypadkach')
        plt.xticks(rotation=45, ha='right')#można
        #   plt.savefig('test.jpg')

        plt.show()

        print("Podsumowanie wykresu")
        procenty=[]
        wszyskie=sum(ilosc)
        for x in ilosc:
            proc=(x/wszyskie)*100#peocenty
            procenty.append(round(proc,2))

        wynik = dict({
             "Typ Pojazdu": wartosc ,
                "ile": ilosc,
                "Udział%":procenty })
        
        wynik=pd.DataFrame(wynik)
        print(wynik)

        odp=str(input("czy chcesz zapisać wynik? T/N "))
        if odp.upper()=="T":
            zapDoCSV(wynik)
        else: print("Anulowano zapis") 


    def obrazenia(self):
        data=self.data
        #4 ile jest/jaki procent rekordów tworzą z znanym uszkodzeniem ciała injury/unknown
        factor=data['Injury_Type']
        factorNP=factor.to_numpy()
        # print(np.unique(factorNP))
        wartosc,ilosc=np.unique(factorNP,return_counts=True)

        plt.figure(figsize=(10, 6))
        plt.bar(wartosc, ilosc)
        plt.ylabel('Ilość przypadków')
        plt.xlabel('typ obrarzeń')
        plt.title('ilość przypadków o podanym typie obrażeń')
        plt.xticks(rotation=0, ha='right')
        #   plt.savefig('test.jpg')
        plt.show()

        print("Podsumowanie wykresu")
        procenty=[]
        wszyskie=sum(ilosc)
        for x in ilosc:
            proc=(x/wszyskie)*100#peocenty
            procenty.append(round(proc,2))

        wynik = dict({
             "Obrarzenia": wartosc ,
                "ile": ilosc,
                "Udziałw%":procenty })
        
        wynik=pd.DataFrame(wynik)
        print(wynik)

        odp=str(input("czy chcesz zapisać wynik? T/N "))
        if odp.upper()=="T":
            zapDoCSV(wynik)
        else: print("Anulowano zapis") 

    def Weekend(self):
        data=self.data
        #5 kiedy zdarza się więcej wypadków na dzień w dnie pracy czy weekendy?
        factor=data['Weekend?']
        factorNP=factor.to_numpy()
        wartosc,ilosc=np.unique(factorNP,return_counts=True)
        
        i=0
        IleNaDzień=[]
        #nie wiem jak na tym etapie podzielić sensownie weekend od worck 
        while i<len(wartosc):
            if i==0:
              IleNaDzień.append(ilosc[i]/5)
            if i==1:
                IleNaDzień.append(ilosc[i]/2)
            i+=1
            


        plt.figure(figsize=(10, 6))
        plt.bar(wartosc, IleNaDzień)
        plt.ylabel('procętowy rozkład przypadków wypadków')
        plt.xlabel('typ obrarzeń')
        plt.title('ilość wypadków występujących w dzień roboczy względem wypadków w dzień weekendowy')
        plt.xticks(rotation=0, ha='right')
        #   plt.savefig('test.jpg')
        plt.show()
        
        print("Podsumowanie wykresu")
    

        wynik = dict({
             "Weekend?": wartosc ,
                "ilePrzyp": ilosc,
                "PrzypNaDzień":IleNaDzień })
        
        wynik=pd.DataFrame(wynik)
        print(wynik)

        odp=str(input("czy chcesz zapisać wynik? T/N "))
        if odp.upper()=="T":
            zapDoCSV(wynik)
        else: print("Anulowano zapis") 

    def ileWypGodz(self):
        data=self.data
    #6 w jakich godzinach dochodzi do największej liczby wypadków albo wykres liniowy z godzinammi ilością wypadków podczas nich. (napraw te godziny)
    #godzin nie przerabiaj tylko podziel je przez 100 i będize wyglądac nadal dobrze bo potrzebujesz tylko kolejności

        factor=data['Hour']
        factorNP=factor.to_numpy()
        wartosc,ilosc=np.unique(factorNP,return_counts=True)
        wartosc=wartosc/100 #poniewarz z jakiegoś popwodu wareości godzinowe są w dziwnym formacie

        plt.figure(figsize=(10, 6))
        plt.plot(wartosc, ilosc, marker='o', linestyle='-', color='b')
        plt.ylabel('rozkład ilośći przypadków wypadków')
        plt.xlabel('Godzina')
        plt.title('Podział przypadków wzglendem godziny')
        plt.xticks(rotation=0, ha='right')
        plt.grid(True)
        plt.show()
        
        print("Podsumowanie wykresu")
        procenty=[]
        wszyskie=sum(ilosc)
        for x in ilosc:
            proc=(x/wszyskie)*100#peocenty
            procenty.append(round(proc,2))

        wynik = dict({
                "Godzina:": wartosc ,
                "ile": ilosc,
                "Udziałw%":procenty })
        
        wynik=pd.DataFrame(wynik)
        print(wynik)

        odp=str(input("czy chcesz zapisać wynik? T/N "))
        if odp.upper()=="T":
            zapDoCSV(wynik)
        else: print("Anulowano zapis")

    def IleWypMies(self):
        data=self.data
        factor=data['Month']

        factorNP=factor.to_numpy()
        wartosc,ilosc=np.unique(factorNP,return_counts=True)
        wartosc=wartosc/100 #poniewarz z jakiegoś popwodu wareości godzinowe są w dziwnym formacie

        plt.figure(figsize=(10, 6))
        plt.plot(wartosc, ilosc, marker='o', linestyle='-', color='b')
        plt.ylabel('rozkład ilośći przypadków wypadków')
        plt.xlabel('Miesiąc')
        plt.title('Podział przypadków wzglendem miesięcy')
        plt.xticks(rotation=0, ha='right')
        plt.grid(True)
        plt.show()

        
        print("Podsumowanie wykresu")
        procenty=[]
        wszyskie=sum(ilosc)
        for x in ilosc:
            proc=(x/wszyskie)*100#peocenty
            procenty.append(round(proc,2))

        wynik = dict({
                "Miesiąc:": wartosc ,
                "ile": ilosc,
                "Udziałw%":procenty })
        
        wynik=pd.DataFrame(wynik)
        print(wynik)

        odp=str(input("czy chcesz zapisać wynik? T/N "))
        if odp.upper()=="T":
            zapDoCSV(wynik)
        else: print("Anulowano zapis") 
        
    def IleWypRok(self):
        data=self.data
        factor=data['Year']
        factorNP=factor.to_numpy()
        wartosc,ilosc=np.unique(factorNP,return_counts=True)
        wartosc=wartosc/100 #poniewarz z jakiegoś popwodu wareości godzinowe są w dziwnym formacie

        plt.figure(figsize=(10, 6))
        plt.plot(wartosc, ilosc, marker='o', linestyle='-', color='b')
        plt.ylabel('rozkład ilości przypadków wypadków')
        plt.xlabel('roku')
        plt.title('Podział przypadków wzglendem roku')
        plt.xticks(rotation=0, ha='right')
        plt.grid(True)
        plt.show()

        print("Podsumowanie wykresu")
        procenty=[]
        wszyskie=sum(ilosc)
        for x in ilosc:
            proc=(x/wszyskie)*100#peocenty
            procenty.append(round(proc,2))

        wynik = dict({
                "Rok:": wartosc ,
                "ile": ilosc,
                "Udziałw%":procenty })
        
        wynik=pd.DataFrame(wynik)
        print(wynik)

        odp=str(input("czy chcesz zapisać wynik? T/N "))
        if odp.upper()=="T":
            zapDoCSV(wynik)
        else: print("Anulowano zapis") 


#7 bedziesz miec godziny wypadkow np to predykcje mozesz zrobic np ze od godzin/miesiąca najczesciej jest distracted kierowca
# data[2:4]#wyb kolumn 
##zapis do csv to będzie dane testowe dla predykcji i dane zpredyktowane w tabelcje jako csv(mam funkcje do tego)

#masz funkcje coś robiącą 
#dane.punkty.apply(funkcja)#punkty to nazwa kolumny

#do klasy prostego menu konsolowego


def zapDoCSV(zapisz):
    path = "C:\\Users\\hubla\\Documents\\studia-pliki\\repozytoria\\ProgPython\\ProjProgPyth\\crashProj\\wynik.csv" 
    #nie najlepszy sposób bo nie mogę zapisać wielu plików może potem: os.path.join(path, "User/Desktop", "file.txt")
    os.path.join(path, "User/Desktop", "file.txt")
    if os.path.exists(path):
        print("taki plik istnieje")
        x= str(input("czy chcesz zamienić zawatrosć pliku? T/N "))
        if x.upper()=='T':
            os.remove(path)

            zapisz.to_csv(path, index=False)
            print("plik został zamieniony")
            
        else: print("anulowano zapis")#nie chciałem tego zapentlić by wymuszać wybór
    else:
        print("Zapisano wynik")
        zapisz.to_csv(path, index=False)
    
def clear():
    os.system('cls')


def menu():
    while True:
        print("\nMenu:")
        print("1. Wyświetl CSV (getdata)")
        print("2. Informacja dotycząca danych")
        print("3. Wykres Ilości Wypadków według powodu ich wydarzenia (IleWypTyp)")
        print("4. Wykres Ilości Wypadków według Pojazdu/uczesnikaruchu (ileAutWyp)")
        print("5. Wykres Ilości obrażeń podczas wypadku (obrazenia)")
        print("6. Wykres Ilości Wypadków według godzin (ileWypGodz)")
        print("7. Wykres Ilości Wypadków według miesięcy (IleWypMies)")
        print("8. Wykres Ilości Wypadków w odniesieniu do lat (IleWypRok)")
        print("9. Wykres porównujący ilość wypadków na dzień w tygodniu a w weekendy")
        print("10. Wyjście")

        choice = input("Wybierz opcję: ")
        
        if choice == '1':
            print(przet.getdata())
        elif choice == '2':
            przet.info()
        elif choice == '3':
            przet.IleWypTyp()
        elif choice == '4':
            przet.ileAutWyp()
        elif choice == '5':
            przet.obrazenia()
        elif choice == '6':
            przet.ileWypGodz()
        elif choice == '7':
            przet.IleWypMies()
        elif choice == '8':
            przet.IleWypRok()
        elif choice=='9':
            przet.Weekend()
        elif choice == '10':
            print("Koniec programu.")
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")

        input("Naciśnikk klawisz, aby kontynuować...")
        clear()


#pobieranie csv
path = 'C:\\Users\\hubla\\Documents\\studia-pliki\\repozytoria\\ProgPython\\ProjProgPyth\\crashProj\\car.csv'
if os.path.exists(path):          
    dane = pd.read_csv(path,dtype={
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
    print("Załadowano plik CSV.")
    dane = pd.DataFrame(dane)
    dane.dropna(inplace=True)#odrzucone rekordy bez wartości 
else:
    print("Brak pliku CSV")
    #jak nie ma nie powinno puszczać dalej zrób w menu

#print(data)
przet=przetwarzanie(dane)
menu()
zapDoCSV(dane)
nowa="nowa zmienna"
# Uruchomienie menu


    #zapisz odpowiedzi na pytania w pliku



