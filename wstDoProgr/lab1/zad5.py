
def dodawanie(a,b):
    return(a+b)

def odejmowanie(a,b):
    return(a-b)

def mnorzenie(a,b):
    return(a*b)

def dzielenie(a,b):
    if b==0:
        return None
    else:
        return(a/b)

slo={"+":dodawanie,
    "-":odejmowanie,
    "*":mnorzenie,
    "/":dzielenie}
x=input("jakie diałanie? ")
a=int(input("pierwsza liczba "))
b=int(input("2 liczba "))
print(slo[x](a,b))

#
# def dodawanie(a,b):
#     return a+b
# def odejmowanie(a,b):
#     return a-b
# def mnozenie(a,b):
#     return a*b
# def dzielenie(a,b):
#     if b == 0:
#         return None
#     else:
#         return a/b
# dzialanie = {'+': dodawanie, '-': odejmowanie, '*': mnozenie, '/': dzielenie}
# x = input("Jakie działanie? ")
# a = int(input("Podaj 1 liczbe: "))
# b = int(input("Podaj 2 liczbe: "))
# print(dzialanie[x](a,b)