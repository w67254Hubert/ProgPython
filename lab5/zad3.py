zwierzeta = []
for i in range(4):
    s = input("Napisz zwierzet, których chcesz dodać: ")
    zwierzeta.append(s)
zwierzeta.sort()
print(zwierzeta[0], zwierzeta[-3: ], len(zwierzeta))
''''''