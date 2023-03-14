# Napisz skrypt, który sprawdzi czy litera wprowadzona przez użytkownika jest duża czy mała.
litera=input("podaj litere ")
if "a"<=litera>='z':
    print("litera jest mała")
elif "A" <= litera <= 'Z':
    print("litera jest durza")
else:
    print("to nie litera")
""