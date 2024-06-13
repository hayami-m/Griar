import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
#style.use('seaborn-ticks')

def string_kernel(x ,y):
    m, n= len(x), len(y)
    S=0
    for i in range(m):
        for j in range(i,m):
            for k in range(n):
                if x[(i-1):j]==y[(k-1):(k+j-i)]:
                    S = S + 1
    return S

C = ["a", "b"]
m = 10
w = np.random.choice(C, m,replace=True)
x, y = "", ""
for i in range(m):
    x = x + w[i]
w = np.random.choice(C, m,replace=True)
for i in range(m):
    y = y + w[i]

print(x,y,string_kernel(x,y))