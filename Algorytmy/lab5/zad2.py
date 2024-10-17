
n= int(input("podaj n"))

tab=[[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        if i>0 and j==0:
            tab[i][j]=0
        elif i==0 and j>0:
            tab[i][j]=1
        else:
            tab[i][j]=(tab[i-1][j]+tab[i][j-1])/2

for row in tab:
    print('     '.join([str(elem,2)for elem in row]))
