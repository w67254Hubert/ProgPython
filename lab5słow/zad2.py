'''Zadanie 2.
• Wypisz wszystkie pary klucz:wartość występujące w słowniku:
sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}
• Utwórz słownik, wybierając ze słownika sample_dict pary o kluczach zapisanych w liście.
Wskazówki:
− przejdź za pomocą pętli po kluczach zapisanych w liście;
− następnie sprawdź, czy dany klucz występuje w słowniku; jeśli występuje, dodaj go (parę
klucz:wartość) do nowego słownika.
• Usuń ze słownika wartości, których klucze występują w liście.
• Sprawdź, czy wartość „Jones” występuje w słowniku.
• Zmień w słowniku klucz ‘city’ na ‘location'''

sample_dict = {"name": "Kelly","surname": "Jones","age": 25,"salary": 8000,"city": "New york"}

for k,v in sample_dict.items():
    print(f'{k:<10} = {v:>10}')
print()

list=["nie ma mnie","age"]

#do podpunktu 2
'''D = {}
for k in list:
    for k2 in sample_dict.keys():
        if(k == k2):
            D[k] = sample_dict[k2]
            break
print(D)'''

'''D = {}
for k in list:
    if k in sample_dict.keys():
        D[k] = sample_dict[k]

print(D)'''
D = {k:sample_dict[k] for k in list if k in sample_dict.keys()}
print(D)
print()

#wersje do jednego podpunktu
#• Usuń ze słownika wartości, których klucze występują w liście.

# for k in list:
#     if k in sample_dict.keys():
#         sample_dict.pop(k)
# print(sample_dict)

for k in list:
        sample_dict.pop(k,None)
print(sample_dict)


#• Sprawdź, czy wartość „Jones” występuje w słowniku.

# if "Jones" in dict1.values():
#     print('element znajduje sie w słowniku')
# else:
#     print('nie ma ')

for k in sample_dict.values():
    if k == "Jones":
        print("istnieje")
        break
else:
    print("nie istnieje")




