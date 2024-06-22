'''Zadanie 3. Napisz funkcję o zmiennej liczbie parametrów, która wyświetla wartości parametrów na ekranie.
Następnie zmodyfikuj funkcję tak, aby znajdowała i zwracała wartość maksymalną.
Wskazówka: użyj parametru *args, który łączy wszystkie dodatkowe (nadmiarowe) argumenty
pozycyjne, niebędące słowami kluczowymi podczas wywoływania funkcji, w krotkę.'''
#cz1
# def zad3(*args):
#     print(args)
#     for i in args:
#          print(i)
#
# zad3()
# zad3(1,3.5,-1,False,[6,6])

#cz2
def max(numer1,*args):
    print(args)
    a = numer1
    for z in args[1:]:
      if z>a:
          a = z
    return(a)

print(max(12,13,14,12,123))
#print(max(s))
