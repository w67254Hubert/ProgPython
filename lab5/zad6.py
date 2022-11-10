'''Zadanie 6.
• Załóżmy, że lista X składa się z 10 elementów. Przenieś ostatnie trzy elementy z końca na początek listy
bez zmiany ich oryginalnej kolejności.
• Utwórz listę Y, wykonując operację: Y = X. Następnie zmień jeden z elementów listy Y. Wyświetl obie listy
na ekranie.'''
x=list(range(10))
print(x)
x[:0]=x[-3:]
#del x[-3:]
x[-3:]=[]
print(x)

y=x
y[4]=12
print(x)
print(y)