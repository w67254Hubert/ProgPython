imiona = ['Kinga', 'Bianka', 'Regina', 'Klementyna', 'Balbina', 'Liliana', 'Ilona', 'Magda', 'Elżbieta', 'Żaneta',
             'Ilona', 'Józefa', 'Judyta','Aneta', 'Lidia', 'Celina', 'Ilona', 'Lara', 'Franciszka', 'Asia', 'Eliza',
             'Teresa', 'Amalia', 'Felicja', 'Celina', 'Bogna', 'Jolanta', 'Faustyna', 'Gabriela', 'Wioletta', 'Blanka',
             'Mirosława', 'Felicja', 'Sylwia', 'Iza', 'Bernadetta', 'Pamela', 'Amelia', 'Weronika', 'Patrycja', 'Andżelika',
             'Agnieszka', 'Stanisława', 'Daria', 'Ola', 'Aneta', 'Teresa', 'Andrea', 'Lila', 'Alicja', 'Liliana',
             'Kajetan', 'Dominik', 'Anatol', 'Eryk', 'Alek', 'Daniel', 'Adam', 'Aleks', 'Leonardo', 'Ludwik',
             'Diego', 'Jarosław', 'Amadeusz', 'Marcin', 'Joachim', 'Grzegorz', 'Anatol', 'Ignacy', 'Gabriel', 'Joachim',
             'Eryk', 'Korneliusz', 'Jerzy', 'Leszek', 'Jacek', 'Aleksy', 'Konrad', 'Joachim', 'Maksymilian', 'Andrzej',
             'Eugeniusz', 'Bronisław', 'Aleks', 'Jakub', 'Bronisław', 'Radosław', 'Leszek', 'Mateusz', 'Alan', 'Alojzy',
             'Emanuel', 'Albert', 'Filip', 'Amir', 'Milan', 'Michał', 'Alan', 'Joachim', 'Michał', 'Allan','Joachim']

nazwisko = ['Sikorska', 'Malinowski', 'Rutkowski', 'Witkowski', 'Ziółkowska', 'Zakrzewska', 'Wójcik', 'Makowski', 'Wróblewski',
                 'Szymański', 'Czarnecki', 'Zakrzewska', 'Jakubowski', 'Lewandowski', 'Górski', 'Wiśniewski', 'Mróz', 'Walczak', 'Czarnecki',
                 'Sikorska', 'Kucharski', 'Sokołowski', 'Kaźmierczak', 'Walczak', 'Baranowski', 'Pawlak', 'Wójcik', 'Szczepański', 'Kowalski',
                 'Borkowski', 'Szulc', 'Sobczak', 'Stępień', 'Zakrzewska', 'Sawicki', 'Sobczak', 'Makowski', 'Kowalski', 'Kubiak', 'Zawadzki',
                 'Baran', 'Kowalczyk', 'Wysocki', 'Chmielewski', 'Stępień', 'Nowak', 'Lewandowski', 'Mróz', 'Zawadzki', 'Czerwiński', 'Szymański',
                 'Szewczyk', 'Krajewska', 'Krajewska', 'Chmielewski', 'Sadowska', 'Czarnecki', 'Chmielewski', 'Kwiatkowski', 'Górecki', 'Błaszczyk',
                 'Woźniak', 'Szewczyk', 'Szymański', 'Sawicki', 'Baranowski', 'Pawlak', 'Woźniak', 'Głowacka', 'Stępień', 'Lis', 'Czarnecki',
                 'Sawicki', 'Lewandowski', 'Kucharski', 'Wójcik', 'Mróz', 'Wiśniewski', 'Szewczyk', 'Szymczak', 'Rutkowski', 'Zakrzewska', 'Mazur',
                 'Mróz', 'Jasiński', 'Duda', 'Szczepański', 'Kamiński', 'Kaczmarczyk', 'Kozłowski', 'Sawicki', 'Górski', 'Włodarczyk', 'Mazurek',
                 'Sikora', 'Malinowski', 'Zawadzki', 'Adamska', 'Włodarczyk', 'Stępień', 'Ostrowski', 'Górski']


import random

numtel = []
e = 102

while e > 0:
    losowa_liczba = random.randint(100000000, 999999999)
    numtel.append(losowa_liczba)
    e -= 1


import random
import string

# Funkcja do generowania losowego adresu e-mail
def generuj_adres_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{username}@user.pl"

# Generowanie 102 adresów e-mail
adresy_email = [generuj_adres_email() for _ in range(102)]

# Wyświetlenie wyniku
pesele = [
    '79071678669', '01261115942', '76110223545', '78031511246', '73103044468',
    '05292411826', '85072684361', '74011245965', '96112728541', '98122653369',
    '80032333846', '81121452381', '85121719828', '99071743325', '10282776625',
    '91051465164', '07261072546', '93032288986', '79082795584', '06322522622',
    '04301926926', '90031593947', '89062892363', '75072757264', '99122993925',
    '94080418426', '12272523541', '91082241384', '81040159325', '98080477681',
    '97082529785', '84012129582', '99022068246', '95112738868', '91052819245',
    '76051572885', '93051515481', '88060194828', '05261374484', '71020165361',
    '06310752961', '10272496483', '09210538989', '06292247664', '91080584429',
    '03252075228', '95020554385', '96090768823', '95093045566', '03262862649',
    '72123148426','79101848899', '03280241439', '00282293112', '00213151595', '79122448298',
    '02310884213', '95070937712', '81111669339', '04291071417', '86041562194',
    '97021831656', '77041933536', '70060244634', '90091548691', '83052417592',
    '08270764758', '05270849456', '91030251414', '87091563678', '78070859938',
    '04232458754', '10272691314', '92072297497', '11211557894', '87092337791',
    '70021158974', '86050997914', '08312113953', '88052524891', '96071815775',
    '99111393732', '88121036755', '72051859575', '82060226534', '71072872776',
    '08210616639', '12292466275', '80091116457', '94123089998', '70121145278',
    '84052091551', '77100521113', '86070696778', '96011747391', '83011537752',
    '87082853339', '01241824897', '08212783236', '84110892177', '04221712276',
    '99072076815'
]

print(len(imiona))
print(len(nazwisko))
print(len(numtel))
print(len(adresy_email))
print(len(pesele))


print("oto moje dane heh")

i=101
while i>=0:
    print("('",imiona[i],"','",nazwisko[i],"',",numtel[i],",'",adresy_email[i],"','",pesele[i],"'),")
    i=i-1