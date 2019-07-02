import numpy as np
import matplotlib.pylab as plt
def relu(x):
    return np.maximum(0,x)
x = np.arange(-0.5,5.0,0.1)
y = relu(x)
plt.plot(x,y)
plt.ylim(-1.0,5.1)
plt.show()