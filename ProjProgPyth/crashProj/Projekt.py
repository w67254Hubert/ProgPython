

#https://www.kaggle.com/datasets/jacksondivakarr/car-crash-dataset/data
#Wczytywanie, analiza i wizualizacja danych wypadków samochodowych. język Python

import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
import seaborn as sns#dalej nie urzyte
import tkinter as tk
from tkinter import messagebox


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
        #dataframe przekazujemy do okna aby go wyświetlić urzytkownikowi

        self.openTextWindow(wynik)
        print(wynik)



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

        self.openTextWindow(wynik)



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

        self.openTextWindow(wynik)
        print(wynik)


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

        wynik = dict({
             "Weekend?": wartosc ,
                "ilePrzyp": ilosc,
                "PrzypNaDzień":IleNaDzień })
        
        wynik=pd.DataFrame(wynik)
        self.openTextWindow(wynik)
        print(wynik)


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
        self.openTextWindow(wynik)

    def IleWypMies(self):
        data=self.data
        factor=data['Month']

        factorNP=factor.to_numpy()
        wartosc,ilosc=np.unique(factorNP,return_counts=True)
        
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
        self.openTextWindow(wynik)
        print(wynik)

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
        self.openTextWindow(wynik)
        print(wynik)

    
#####################################
#tworzenie gui
    def gui(self):
        self.main_window = tk.Tk()
        # Utworzenie widżetu okna głównego.
        # Wejście do pętli głównej tkinter.
        self.main_window.title('Program do analizy danych wypadków samochodowych')
     
        self.labelp = tk.Label(self.main_window, text='Program do analizy danych wypadków samochodowych')
        self.labelp.pack(side='top')

        self.my_button1 = tk.Button(self.main_window,text='Pokaż Wykres ilości typów wypadków',command=lambda: self.IleWypTyp())
        self.my_button1.pack()

        self.my_button2 = tk.Button(self.main_window,text='Pokaż Wykres ilości poszczególnych uczestników wypadków',command=lambda: self.ileAutWyp())
        self.my_button2.pack()

        self.my_button3 = tk.Button(self.main_window,text='Pokaż Wykres jak często występują obrarzenia ciała',command=lambda: self.obrazenia())
        self.my_button3.pack()

        self.my_button4 = tk.Button(self.main_window,text='Pokaż Wykres ile wypadków wypada na dzień w weekend/zwykły dzień',command=lambda: self.Weekend())
        self.my_button4.pack()

        self.my_button5 = tk.Button(self.main_window,text='Pokaż Wykres ilości wypadków co do godziny',command=lambda: self.ileWypGodz())
        self.my_button5.pack()

        self.my_button6 = tk.Button(self.main_window,text='Pokaż Wykres ilości typów w danych miesiącach',command=lambda: self.IleWypMies())
        self.my_button6.pack()

        self.my_button7 = tk.Button(self.main_window,text='Pokaż Wykres Wypadków na rok',command=lambda: self.IleWypRok())
        self.my_button7.pack()


        self.quit_button = tk.Button(self.main_window,text='Zakończ Analize',command=self.main_window.destroy)
        self.quit_button.pack()

        tk.mainloop()

    def openTextWindow(self,text):#strasznie dziwnie formatuje podanego dataframe
        self.text = text

        self.top_level = tk.Toplevel(self.main_window) 

        self.top_level.title("Podsumowanie do wykresu")
        # Tworzymy etykietę, która będzie wyświetlać tekst
        label = tk.Label(self.top_level, text=text)
        # Umieszczamy etykietę w oknie
        label.pack(padx=10, pady=10)

        self.top_level.protocol("WM_DELETE_WINDOW", self.askToSaveFile)
        self.top_level.wait_window()


    def askToSaveFile(self):
        # Tworzymy główne okno aplikacji
        self.main_window.deiconify()
        self.top_level.withdraw()
        # Wyświetlamy okno dialogowe z zapytaniem
        response = messagebox.askquestion("Zapisywanie pliku", "Czy chcesz zapisać ten plik?")
        # Sprawdzamy odpowiedź użytkownika
        if response == "yes":
            print("Wybrano: Tak")
            self.saveToCSV(self.text)
            # Tutaj możesz dodać kod do zapisania pliku
        else:
            print("Wybrano: nie")

        # Zamykamy główne okno aplikacji (nie jest konieczne, jeśli aplikacja nie będzie miała innych elementów)
        self.top_level.destroy()
   ##################################

    def saveToCSV(self,zapisz):
        path = "C:\\Users\\hubla\\Documents\\studia-pliki\\repozytoria\\ProgPython\\ProjProgPyth\\crashProj\\wynik.csv" 
        #nie najlepszy sposób bo nie mogę zapisać wielu plików może potem: os.path.join(path, "User/Desktop", "file.txt")
        os.path.join(path, "User/Desktop", "file.txt")
        if os.path.exists(path):
            root = tk.Tk()
            root.withdraw() 
            response = messagebox.askquestion("Zapisywanie pliku", "Plik istnieje czy nadal chcesz go zapisać?")
            # Sprawdzamy odpowiedź użytkownika
            if response == "yes":
                os.remove(path)
                zapisz.to_csv(path, index=False)
                print("plik został zamieniony")
            else:
                print("anulowano zapis")
            root.destroy()

        else:
            print("Zapisano wynik")
            zapisz.to_csv(path, index=False)
    

#menu konsolowe nie jest już wykorzystywane
def clear():
    os.system('cls')
def menu():
    while True:
        print("\nMenu:")
        print("1. Wyświetl CSV (getdata)")
        print("2. Informacja dotycząca danych")
        print("3. Uruchominie GUI Do analizy wykresów")
        print("4. Wyjście")
        

        choice = input("Wybierz opcję: ")
        
        if choice == '1':
            print(przet.getdata())
        elif choice == '2':
            przet.info()
        elif choice == '3':
            przet.gui()
            break
        elif choice == '4':
            print("Koniec programu.")
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")

        input("Naciśnikk klawisz, aby kontynuować...")
        clear()

#pobieranie danych z pliku csv 
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

#print(data)

#urworzenie klasy przetwarzanie
przet=przetwarzanie(dane)
menu()





