'''Utwórz listę values zawierającą liczby 10, 20, 30. Utwórz drugą listę keys zawierającą nazwy tych liczb w
języku angielskim (lub polskim). Dokonaj konwersji tych list w słownik.
Wskazówki:
− użyj funkcji zip(), która pobiera dwie sekwencje (takie jak list, dict, str), łączy je w krotki (pary) i
zwraca;
− lub wykonaj iterację listy za pomocą pętli for i funkcji range(). W każdej iteracji dodaj nową parę kluczwartość do słownika.
• Utwórz drugi słownik metodą słów kluczowych ( dict(klucz1=wartość1, klucz2=wartość2)), gdzie kluczem
będą nazwy liczb 30, 40, 50, a wartościami – liczby 30, 40, 50.
• Połącz dwa słowniki w jeden nowy słownik.'''

values=[10, 20, 30]

keys=["ten","twenty", "therty"]

slownik=dict(zip(values,keys))

print(slownik,"słownik1")


values2=(30,40,50)
keys2=["ten","twenty", "therty"]
slow2={}

for i in range(len(values2)):
  slow2[keys2[i]]=values2[i]

print(slow2 ,"słownik2")
print()

slow_3=dict(thert=30, forty=40, fifty=50)
slow_4=slownik.copy()
slow_4.update(slow2)
print(slow_4,"słownik 4")



