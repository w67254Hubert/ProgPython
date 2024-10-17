
a = [-2,0,4,-3,2,7]
n=6
i=0
while i<n-1:
# for i in range(n-1,0,-1):   
    # print('i w for',i)
    element=a[i]

    j=i-1
    # print('j w wile',j)
    while j>=0 and a[j]>element:
        # print(a[j],'> true',element)
        a[j+1]=a[j]

        # print("j",j)
        
        j=j-1
        print(a)


        # print('i',i)
        # print('eleement w wile',element)
    a[j + 1] = element
    # print('element',element)
    i=i+1
    print("końcowa tabela",a)


