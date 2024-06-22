'''zadanie 3.
• Utwórz słownik składany, którego klucze są liczbami od 1 do 15 (włącznie), a wartości są kwadratami tych
kluczy (1:1, 2:4, 3:9 itd).
• Utwórz drugi słownik składany o kluczach od 0 do 10, i wartościach będących kolejnymi potęgami 2 (np.
0:1, 1:2, 2:4, 3:8, 4:16 itd.). '''

slownik1={x: x*x for x in range(1,16)}
print(slownik1)
slownik2={x: 2**x for x in range(10)}
print(slownik2)

