'''Zadanie 2. Napisz funkcje oblicz(), która ma dwa parametry i oblicza ich sumę oraz różnicę. Ponadto zwraca
jednocześnie jak wynik dodawania, tak i odejmowania'''

def oblicz(x,y):
    S=x+y
    R=x-y
    return(S,R)

print(oblicz(20,10))

x,y = oblicz(2,3)
print(f"Suma = {x}, Roznica = {y}")

# def oblicz(a,b):
#     suma = a+b
#     roznica = a-b
#     return suma, roznica
# print(oblicz(10,5))
# x,y = oblicz(3,2)
# print(f"Suma = {x}, Roznica = {y}")