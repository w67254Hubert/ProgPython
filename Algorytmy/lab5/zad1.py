
tab=[]
n=4
for i in range(n):
    if i==0:
        tab.append(i)
    elif i==1:
        tab.append(i)
    else: tab.append(tab[i-1]+tab[i-2])

print(tab)
