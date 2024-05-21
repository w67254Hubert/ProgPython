daty = [
    '11-01-2023', '11-12-2022', '23-09-2019', '03-03-2018', '07-07-2021',
    '24-08-2021', '28-09-2019', '24-12-2022', '19-07-2023', '07-01-2023',
    '28-11-2020', '14-03-2022', '04-11-2019', '12-05-2020', '06-09-2022',
    '16-01-2020', '25-09-2019', '03-10-2019', '06-01-2020', '23-11-2018',
    '07-08-2019', '14-01-2018', '25-06-2019', '31-01-2023', '17-01-2020',
    '27-02-2018', '08-10-2021', '08-03-2019', '03-02-2022', '16-01-2020',
    '08-09-2022', '27-05-2023', '29-09-2019', '04-10-2018', '29-09-2023',
    '06-07-2018', '15-05-2022', '24-05-2022', '14-03-2019', '18-10-2019',
    '16-01-2020', '29-04-2023', '12-08-2019', '17-09-2019', '07-12-2022',
    '02-07-2018', '29-07-2019', '16-11-2023', '18-09-2018', '23-06-2022',
    '13-01-2020', '25-06-2023', '23-03-2020', '23-07-2019', '31-10-2021',
    '10-05-2019', '10-08-2018', '06-09-2023', '19-05-2022', '16-11-2022',
    '31-01-2018', '12-02-2020', '11-02-2020', '26-04-2021', '17-08-2023',
    '07-11-2022', '02-12-2018', '21-09-2020', '12-07-2020', '20-10-2019',
    '27-01-2018', '27-09-2021', '05-04-2018', '23-05-2019', '10-05-2023',
    '05-03-2023', '29-01-2022', '03-07-2023', '14-06-2020', '22-07-2018',
    '17-10-2021', '29-06-2023', '24-06-2020', '01-10-2021', '11-02-2023',
    '20-04-2022', '18-07-2020', '14-04-2018', '13-03-2019', '21-04-2018',
    '24-03-2020', '25-04-2021', '30-01-2022', '18-11-2019', '22-11-2022',
    '29-02-2020', '22-04-2023', '02-02-2020', '05-05-2018', '16-07-2019'
]


nowe_daty = [f'{rok}-{miesiac}-{dzien}' for dzien, miesiac, rok in (data.split('-') for data in daty)]
popdata=[]
# Wyświetl nowe daty
for data in nowe_daty:
    popdata.append(nowe_daty)
print(nowe_daty)

# pozycje_zawodowe = [
#     "Kierowca",
#     "Księgowy",
#     "Kierownik_Floty",
#     "Inspektor_Biletów",
#     "Biuro_Obsługi_Klienta",
#     "Technik_Pojazdów",
#     "Planista_Tras",
#     "Prezes"
# ]
# i=len(pozycje_zawodowe)-1
# while i>=0:
#     print("('",pozycje_zawodowe[i],"'),")
    # i=i-1

# def sprawdz_powtarzanie(tablica):
#     if len(tablica) == len(set(tablica)):
#         print("Wszystkie elementy tablicy są unikalne.")
#     else:
#         print("W tablicy występują powtarzające się elementy.")

# # Przykładowa tablica
# przykladowa_tablica = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sprawdz_powtarzanie(lista_nieparzystych)

# def sprawdz_przekroczenie(tablica, wartosc):
#     if any(element > wartosc for element in tablica):
#         print("Wartość przekroczona w tablicy.")
#     else:
#         print("Żadna wartość nie przekracza podanej wartości.")

# # Przykładowa tablica
# przykladowa_tablica = lista_nieparzystych
# # Przykładowa wartość do porównania
# przykladowa_wartosc = 72

# # Sprawdź, czy jakakolwiek wartość przekracza podaną wartość
# sprawdz_przekroczenie(przykladowa_tablica, przykladowa_wartosc)

