import numpy as np

def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

a = np.array([0.3,2.9,4.0])
print(softmax(a))

def soft_max(b):
    c = np_max(b)

    exp_b = np.exp(b - c)

    sum_exp_b = np.sum(exp_b)
    y = exp_b / sum_exp_b
    return y

b = np.array([0.3,2.9,4.0])
print(softmax(a))
