def maxW(l , r, tab):
    if l==r: 
        return tab[l]
    m=(l+r+1)//2
    maxR=maxW(l ,m, tab )
    maxL=maxW(m-1 ,r ,tab)
    #to był test lekko przerobionego zadania 3
    
    s=maxR+maxL 
    return s

tab = [3, 5, 2, 8, 1, 7, 9, 4] #suma podancyh liczb to 39
r=0
l=len(tab)-1
print("suma tablicy to", maxW(l, r , tab))