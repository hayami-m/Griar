import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
#style.use('seaborn-ticks')

def C(i,j):
    S, T =s[i],t[j]
    # 頂点のラベルが一致しない場合
    if S[0] != T[0]:
        return 0
    # 頂点が子孫を持たない場合
    if S[1] is None:
        return 0
    if T[1] is None:
        return 0
    if len(S[1]) != len(T[1]):
        return 0
    U = []
    for x in S[1]:
        U.append(s[x][0])
        U1= sorted(U)
    V = []
    for y in T[1]:
        V.append(t[y][0])
        V1 = sorted(V)
    
    m = len (U)
    for h in range(m):
        # 子孫のラベルが一致しない場合
        if U1[h] != V1[h]:
            return 0
    
    U2 = np.array(S[1])[np.argsort(U)]
    V2 = np.array(T[1])[np.argsort(V)]

    W = 1
    for h in range(m):
        W = W * (1 + C(U2[h],V2[h]))
        return W
    
def k(s, t):
    m, n = len(s), len(t)
    kernel = 0
    for i in range (m):
        for j in range(n):
            if C(i,j)>0:
                kernel = kernel + C(i,j)
    return kernel

s = [[] for _ in range(6)]
s[0] = ["G",[1, 3]]; s[1] = ["T", [2]]; s[2] = ["C", None]
s[3] = ["A",[4, 5]]; s[4] = ["C", None]; s[5] = ["T", None]

t = [[] for _ in range(9)]
t[0] = ["G",[1, 4]]; t[1] = ["A", [2, 3]]; t[2] = ["C", None]
t[3] = ["T",None]; t[4] = ["T", [5,6]]; t[5] = ["C", None]
t[6] = ["A",[7, 8]]; t[7] = ["C", None]; t[8] = ["T", None]

for i in range(6):
    for j in range(9):
        if C(i,j)>0:
            print(i,j,C(i,j))

print(k(s,t))

print(k(s,s))