#pierwsza myśl znajduje minimalną ale nie mam pomysłu jak zaimplementować zmianę wartości
'''
import numpy as np

lista=np.array([[0,-2,0,4,3,5,],[6,7,-9,8,-2,9]])

i=0
for x in lista:
    for y in x:
        if y<lista[i,0]:
            lista[i,0]=y
    i=i+1   

print(lista[1,0])
print(lista[0,0])
'''
# drugie podejście po edukacji że jednak nie potrzebuje nupmy by stworzyć tablice wielowymiarową.

lista = [[0,-2,0,4,3,5,],[6,7,-9,8,-2,9]]

for x in lista:
    minim = min(x)
    i = x.index(minim)
    x[0], x[i] = x[i], x[0]

print(lista)