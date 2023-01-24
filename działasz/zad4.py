
a="kalka"

def znaki(a):
    s={}
    for x in a:
        if x in s:
            s[x] =+1
        else:
            s[x]=1
    return s

print(znaki(a))