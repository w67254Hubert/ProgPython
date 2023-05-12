def find(a,b):
    l = []
    for x in range(len(a)):
        if a[x] == b:
            l.append(x)
    return l
print(find([10,3,5,8,5,5],5))
L = [1,3,4,3,5]
wynik = find(L,3)
print(wynik)