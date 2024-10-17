#wersja pierwsza nwdIteracyjne
def nwdIter(a,b):
    while a!=b:
        if a>b: a=a-b
        else: b=b-a
    return a

print(nwdIter(12,18))
print(nwdIter(28,24))

# wersja  rekurencyjnie
def nwdRek(a,b):
    if a!=b:
        if a>b: return nwdRek(a-b,b) #a=a-b
        else: return nwdRek(a,b-a) #b=b-a
    return a

print(nwdRek(12,18))

# 2 wersja iterowanego

def nwditerII(a,b):
    while b!=0:
        temp=b
        b=a%b
        a=temp
    return a

# 2 wersja rekurencyjnego

def nwdrekII(a,b):
    if b!=0:
        return nwdrekII(b,a%b)
    return a
##wersja pierwsza nwdIteracyjne
def nwdIter(a,b):
    while a!=b:
        if a>b: a=a-b
        else: b=b-a
    return a

print(nwdIter(12,18))
print(nwdIter(28,24))

# wersja  rekurencyjnie
def nwdRek(a,b):
    if a!=b:
        if a>b: return nwdRek(a-b,b) #a=a-b
        else: return nwdRek(a,b-a) #b=b-a
    return a

print(nwdRek(12,18))

# 2 wersja iterowanego

def nwditerII(a,b):
    while b!=0:
        temp=b
        b=a%b
        a=temp
    return a

# 2 wersja rekurencyjnego

def nwdrekII(a,b):
    if b!=0:
        return nwdrekII(b,a%b)
    return a
#