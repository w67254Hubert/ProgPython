# #odwracaine tablicy w funkcji za pomocą while

def odwracanie(tab):
    start = 0
    end = len(tab) - 1
    while start < end:
        tab[start], tab[end] = tab[end], tab[start]
        start=start+1
        end=end-1

tab = [1, 2, 3, 4, 5]
odwracanie(tab)
print("tab po funkcji odwaracanie", tab) #porządany wynik: [5, 4, 3, 2, 1]




#odwrucenie tablicy w funkcji rekurencjnnie
def RekOdw(tab, start, end):
    if start >= end:
        return
    tab[start], tab[end] = tab[end], tab[start]
    RekOdw(tab, start+1, end-1)

tab2 = [1, 2, 3, 4, 5]
start=0 #tablica zaczyna sie od 0
end=len(tab2)-1 #len -1 poniewarz liczymy od zera a funkcja len liczy od 1
RekOdw(tab2, start, end) #musimy zmienne start i end zdefiniować przed wejściem do funkcji by się nie "resetowały"
print("tab2 po funkcji RekOdw",tab2) #porządany winik [5, 4, 3, 2, 1]

