

def maxW(l , r, W):
    if l==r: 
        return W[l] #zwraca wartość gdy indeksy r i l są równe
    m=(l+r+1)//2
    maxR=maxW(l ,m, W )
    maxL=maxW(m-1 ,r ,W) 
    
    if maxL>maxR: return maxL 
    else: return maxR


W = [3, 5, 2, 8, 1, 7, 9, 4] #największa liczba to 9
r=0
l=len(W)-1
print("max wartoś wektora to", maxW(l, r , W))

