
def hanoi(n, z, na, tym):
    if n == 1:
        print("Przenoszę dysk z", z, "na", na)
    else:   
        hanoi(n-1, z, tym, na)
        print("Przenoszę dysk z", z, "na", na)
        hanoi(n-1, tym, na, z)

n=4 #n to piętra wierzy 
#chcemy przenieść wszystkie krąrzki z A na C a B jest kołkiem tymczasowym
hanoi(n, "A", "C", "B") 
