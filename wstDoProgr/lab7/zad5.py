import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-(np.pi), np.pi, 100)
y = np.sin(x)
plt.plot(x, y)
#plt.plot(x, np.sin(x)*2)
#plt.plot(x, np.sin(x)+2)
plt.plot(x, np.sin(2*x))
plt.show()