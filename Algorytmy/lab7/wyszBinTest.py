# urzytkownik podaje liczbe n - ilość elemantów w liście, n>0
#
# 2 elementy listy losujemy z przedziału x y
# podaje je urzytkownik , należy spr warunek czy zbiór jest dobrze podany
#
# nalerzy wyświtlić liste wylosowaną oraz posortowaną
# urzytkownik podaje liczbę szukaną x
#
# program wyświetla informacje o znaleźeniu lidzby i na jakiej pozycji jest jeżeli nie też wyśfietl komunikat

import random

def quicksort(l, r, list):
    if l >= r:
        return

    v = list[r]
    p = l

    for j in range(l, r):
        if list[j] < v:
            list[p], list[j] = list[j], list[p]
            p += 1

    list[p], list[r] = list[r], list[p]

    quicksort(l, p - 1, list)
    quicksort(p + 1, r, list)
    return list


def binarysearch(lista,left,right,szukana):
    left=0
    right=n-1
    srodek=(left+right)//2
    while left<=right:
        srodek = (left + right) // 2
        if lista[srodek] ==szukana:
             return srodek
        elif lista[srodek]>szukana:
            right=srodek-1
        else:
            left=srodek+1

    return -1
def randlis(x,y,n):
    lis=[]
    k=n
    while k>0:
        a=random.randint(x,y)
        lis.append(a)
        k=k-1
        
    return lis


n= int(input("podaj długość listy"))

while n<=0:
    n=int(input("podaj liczbę większą od 0"))


x=int(input("podaj początek przedziału liczb"))
while x is int:
    x=int(input("podaj x początek przedziału liczbe, liczbę większą lub równą 0"))


y=int(input("podaj końcową liczbe przedziału liczb"))
while y<x:
    x=int(input("podaj początek przedziału liczbe, liczbę większą od x"))



lis=randlis(x,y,n)

#to jest strasznie nieoptymalne ale chyba tak i był zamysł zadania?     


while True:
    lis.clear()
    liczDup=0

    lis=randlis(x,y,n)

    for i in range(n):
        for j in range(i + 1, n):
            if lis[i] == lis[j]:
                liczDup = liczDup + 1
    if liczDup == 0:
        break
#


quicksort(0,n-1,lis)
print(lis)


szuk=int(input(" czego szukasz"))

wynikSzuk=binarysearch(lis,0,n-1,szuk)
print("szukana liczba występuje na indeksie: ",wynikSzuk)
