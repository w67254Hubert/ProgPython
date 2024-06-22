'''Zadanie 1. Konwersja 8-bitowej liczby binarnej na liczbę dziesiętną.
• Utwórz 8-elementową listę składaną o wartościach będących kolejnymi potęgami dwójki - [128 64 32
16 8 4 2 1]
• Na podstawie tej listy utwórz tablice ndarray o nazwie wagi.
• Utwórz drugą 8-elementową tablicę ndarray wypełnioną zerami i jedynkami (losowo) o nazwie
liczba_bin.
• Oblicz iloczyn tablic wagi i liczba_bin, a następnie policz sumę wartości iloczynu.'''


import numpy as np

potengi2=[]

for i in range(7,-1,-1):
    potengi2.append(2**i)
print(potengi2)

wagi = np.array(potengi2)
print(wagi)

liczba_bin= np.random.randint(low=0 ,high=2 ,size=8)
print(liczba_bin)

ilocczyntab = (liczba_bin * wagi)
print(ilocczyntab)

dec=sum(ilocczyntab)
print(dec)

print(dec.sum())


