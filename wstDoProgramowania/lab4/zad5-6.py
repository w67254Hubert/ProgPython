n = int(input("Proszę podać liczbę studentów: "))
a = 1 #wyświetlanie od 1 studenta
c = 0 #podstawienie pod dodawanie punktów
while True:
    b = int(input(f"Proszę podać punkty studenta {a}: "))
    if b<0 or b>100:
        continue
    c += b #sumowanie punktów studentów
    a += 1 #przechodzenie do kolejnego studenta
    if a == n+1:
        break
y = c/n #obliczanie średniej
print("Średnia wszystkich studentów",y)