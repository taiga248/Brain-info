import numpy as np
def AND(x1,x2):
   x = np.array([x1,x2])
   w = np.array([0.5,0.5])

   print("")
   print(x)
   print(w)

   #バイアス値 発火しやすいよう調整
   b = -0.7
   #ブロードキャスト
   # ex (1,1) , (1*0.5 + 1*0.5)+b = 0.3  発火
   y = np.sum(w*x) + b
   if y <= 0:
      return 0
   else:
      return 1

print(AND(0,0))
print(AND(1,0))
print(AND(0,1))
print(AND(1,1))
