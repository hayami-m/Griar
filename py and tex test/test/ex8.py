import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
#style.use('seaborn-ticks')

def K(x, y, sigma2):
    return np.exp(-np.linalg.norm(x-y)**2/2/sigma2)

def f(z,lam):
    S = 0 ; T = 0
    for i in range(n):
        S = S + K(x[i], z, lam) * y[i]
        T = T + K(x[i], z, lam)
    if T!=0: 
        return S / T
    else:
        print("EROOR")
        return 0

n=1000
x=2*np.random.normal(size=n)
y = np.sin(2 * np.pi * x) + np.random.normal(size=n) / 4

# m = int(n/10)
m = int(n/1000)
sigma2_seq = np.arange(0.001, 0.01, 0.001)
SS_min = np.inf
for sigma2 in sigma2_seq:
    SS = 0
    # for k in range(10):
    for k in range(1000):
        test = range(k * m, (k+1) * m)
        train = [x for x in range(n) if x not in test]
        for j in test:
            u, v = 0, 0
            for i in train:
                kk = K(x[i],x[j], sigma2)
                u = u + kk * y[i]
                v = v + kk
            if not(v==0):
                z = u/v
                SS = SS + (y[j]-z)**2
    if SS<SS_min:
        SS_min = SS
        sigma2_best = sigma2
print("best sigma2 =", sigma2_best)

# 描画設定
plt.figure(num=1, figsize=(15, 8), dpi=80)
plt.xlim(-3,3); plt.ylim(-2,3)
plt.xticks(fontsize=14); plt.yticks(fontsize=14)
plt.scatter(x,y, facecolors="none", edgecolors="k", marker="o")

xx=np.arange(-3, 3, 0.1)
yy=[]
color = "g"
for zz in xx:
    yy.append(f(zz, sigma2_best))
plt.plot(xx,yy, c=color, label=sigma2_best)

plt.legend(loc="upper left", frameon=True, prop={"size":14})
plt.title("Nadaraya-Watson Estimater",fontsize=20)

plt.show()