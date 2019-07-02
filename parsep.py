import numpy as np
import matplotlib.pylab as plt

X = np.array([1.0,1.5])
W1 = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
B1 = np.array([0.1,0.2,0.3])

print(X.shape)
print(W1.shape)
print(B1.shape)

A1 = np.dot(X,W1) + B1

def sigmoid(x):
    return 1 / (1+ np.exp(-x))
x = np.arange(-0.5,5.0,0.1)
y = sigmoid(x)
#plt.plot(x,y)
#plt.ylim(-0.1,1.1)
#plt.show

