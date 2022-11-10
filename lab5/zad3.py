'''Zadanie 3. Utwórz pustą listę zwierzeta. Następnie
• Dodaj kilka nazw zwierząt do listy
• Posortuj listę
• Wyświetl pierwszy oraz trzy ostatnie elementy na liście
• Wyświetl informację o liczbie zwierząt na liście'''

zwierzeta = []
for i in range(4):
    s = input("Napisz zwierzet, których chcesz dodać: ")
    zwierzeta.append(s)
zwierzeta.sort()
print(zwierzeta[0], zwierzeta[-3: ], len(zwierzeta))
''''''