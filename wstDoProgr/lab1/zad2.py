def sum_of_values(dict1):
    suma = 0
    for x in dict1.values():
        suma += x
    return suma
dict1 = {'data1':10, 'data2':-4, 'data3':2}
dict2 = {'data4': 12, 'data5': 10, 'data6': 4}
print(sum_of_values(dict2))