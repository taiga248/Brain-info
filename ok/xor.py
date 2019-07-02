import numpy as np
def NAND(n1,n2):
   x = np.array([n1,n2])
   w = np.array([-0.5,-0.5])
   b = 0.7
   y = np.sum(w*x) + b
   if y <= 0:
      return 0
   else:
      return 1

def AND(a1,a2):
   x = np.array([a1,a2])
   w = np.array([0.5,0.5])
   b = -0.7
   y = np.sum(w*x) + b
   if y <= 0:
      return 0
   else:
      return 1

def OR(o1,o2):
    x = np.array([o1,o2])
    w = np.array([0.5,0.5])
    b = -0.2
    y = np.sum(w*x) + b
    if y <= 0:
        return 0
    else:
        return 1

def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND(s1,s2)
    return y

print(XOR(0,0))
print(XOR(1,0))
print(XOR(0,1))
print(XOR(1,1))
