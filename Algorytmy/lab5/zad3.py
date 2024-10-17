
n=int(input("podaj n "))

tab=[]

for i in range(n):
    for i in range(n):
        if i==0:
            tab.append(1)
        elif i==1:
            tab.append(1)
        else:
            tab.append((2*tab[i-1])-tab[i-2])

print(tab[n])
