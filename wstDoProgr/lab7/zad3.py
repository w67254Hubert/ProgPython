'''3. Utwórz tablicę wypełnioną zerami. Wypełnij zaznaczone obszary tablicy jedynkami.
'''

import numpy as np

tab=np.zeros([3,3])
print(tab)

print()

#1 kratka
'''tab[1:,:2] = 1
print(tab)'''

#2 kratka

#3 kratka

#4 kratka


#5 kratka

import numpy as np
table = np.zeros([3, 3])
print(table)
#table[1:, :2] = 1
#table[:, 2:] = 1
#table[:2, :] = 1
#table[:2, :1] = 1
#table[:2, ::2] = 1
table[:2, [0, 2]] = 1
#table[:2, 2] = 1
print(table)