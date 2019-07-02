import numpy as np
A = np.array([[1,2],[3,4]])
print(A)
A.shape
A.dtype

print("----------")

B = np.array([[3,0],[6,0]])
print(A + B)
print(A * B)
print(A * 10)

print("----------")

P = np.array([[51,55],[14,19]])
print(P[0])
print(P[0][1])

print("----------")

P = P.flatten()
P = np.array([0,2,4])
print(P[P > 15])

print("----------")
import matplotlib.pyplot as plt
x = np.arange(0,6,0.1)
y = np.sin(x)

plt.plot(x,y)
plt.show()
print("Hello Taiga!!!!")
plt.close()
