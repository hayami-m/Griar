import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
#style.use('seaborn-ticks')


# 行列をそのadjointと掛け合わせる
n=3
B=np.random.normal(size=n**2).reshape(3,3)
A=np.dot(B.T,B)
values, vectors = np.linalg.eig(A)
print("values:\n",values,"\n\nvectors:\n",vectors,"\n")

# generate random vector and compute 2-form
S=[]
for i in range (5):
    z=np.random.normal(size=n)
    y=np.squeeze(z.T.dot(A.dot(z)))
    S.append(y)
    if (i+1)%5==0:
        print("S[%d:%d]:" % ((i-4),i),S[i-4:i])
