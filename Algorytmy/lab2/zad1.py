# using System;
# using arra
# a = {-2,0,4,-3,2,7};
# n = 6;

# for (i=0; i<n-1 ;i++)
# {
#     min=i;
#     printf(i)
#     for(j=i+1;j<n;j++){

#         if(a[j]<a[min]) {
#             min=j;
#             }
#     }

#     t=a[min]
#     a[min]=a[i]
#     a[i]=t
# } 
#kod przerobiony na python

a = [-2,0,4,-3,2,7]
n = 6
i=0

while i<(n-1):
    # print("zmiany i", i)
    min=i
    print(min)

    j=i+1
    
    while j<n:
        # print("zmmiany j", j)
        if a[j]<a[min]:
            # print(a[j],"zkjcbsdkfkjsdhfjkdhjk<",a[min])
            min=j

        j=j+1
    
    # print(a)
    # print('whule',min)

    t=a[min]
    a[min]=a[i]
    a[i]=t
    print(a)
    i=i+1
print("nowa tablica", a)
