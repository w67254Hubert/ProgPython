'''Zadanie 2.
• Utwórz losową macierz o wymiarach 5x5. Znajdź największy i najmniejszy element. (patrz tab4_2d;
metoda max(), min())
• Wypisz największe elementy w każdym z wierszy (axis = 1) i w każdej z kolumn (axis = 0).
• Policz sumę wartości w p  oszczególnych wierszach.'''
import numpy as np

macierz= np.random.randint(low=0 ,high=50 ,size=(5,5))
print(macierz)

print("wartość max" ,macierz.max())
print("wartość min" ,macierz.min())

print("wartość max w wierszu" ,macierz.max(axis=1))
print("wartość max w kolumnie" ,macierz.max(axis=0))

print("suma wartośi w wierszach", macierz.sum(axis=1))

