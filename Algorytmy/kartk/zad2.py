
tab=[2,-2,4,5,6,7,8,6,5,4]
i=1
min=tab[0]
while i<10:
    if tab[i]>min:
        pass
    else:
        min=tab[i]
        ind=i
    i=i+1
print("minimalna ",min,"index",ind)