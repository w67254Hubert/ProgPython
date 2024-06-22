
def potenga(lista1,lista2):
    lista3=[]
    if len(lista1)==len(lista2):
        for x in range(len(lista1)):
            lista3.append(lista1[x]**lista2[x])
    else:
         return None
    return lista3

lista1=[2,2,3]
lista2=[0,1,1]
print(potenga(lista1,lista2))