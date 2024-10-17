n = int(input('Podaj ile węzłów ma graf\n n = '))
s = int(input('Podaj węzeł startowy\n s = '))
print('Podaj elementy macierzy:')
macierz = []
for i in range(0, n):
  tab = [int(x) for x in input().split()]
  macierz.append(tab)
print(macierz)
