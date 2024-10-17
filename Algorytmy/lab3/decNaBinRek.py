

def DecNaBin(a):
    if a == 0:
        return []
    wynik = DecNaBin(a // 2)
    wynik.append(a % 2)
    return wynik   

print(DecNaBin(64))

