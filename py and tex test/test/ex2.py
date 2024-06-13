import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
#style.use('seaborn-ticks')

# 設定    
n = 250
x = 2 * np.random.normal(size=n)
y = np.sin(2 * np.pi * x) + np.random.normal(size=n) / 4

def D(t):
    return np.maximum(0.75 * (1 - t**2), 0)

def k(x,y,lam):
    ## Epanechinikov
     return D(np.abs((x-y)/lam))
    ## 指数型
    #return np.exp(lam * np.squeeze(x.T.dot(y)))
    ## Gauss
    # return np.exp((-1 / lam**2) * np.linalg.norm(x-y,ord=2)**2)
    ## 多項式
    #return (np.squeeze(x.T.dot(y))+1)**lam

def f(z,lam):
    S = 0 ; T = 0
    for i in range(n):
        S = S + k(x[i], z, lam) * y[i]
        T = T + k(x[i], z, lam)
    if T!=0: 
        return S / T
    else:
        print("EROOR")
        return 0
    

# 描画設定
plt.figure(num=1, figsize=(15, 8), dpi=80)
plt.xlim(-3,3); plt.ylim(-2,3)
plt.xticks(fontsize=14); plt.yticks(fontsize=14)
plt.scatter(x,y, facecolors="none", edgecolors="k", marker="o")


xx=np.arange(-3, 3, 0.1)
yy=[[]for _ in range(3)]
lam=[0.05,0.35,0.50]
color = ["g","b","r"]
for i in range(3):
    for zz in xx:
        yy[i].append(f(zz, lam[i]))
    plt.plot(xx,yy[i], c=color[i], label=lam[i])

plt.legend(loc="upper left", frameon=True, prop={"size":14})
plt.title("Nadaraya-Watson Estimater",fontsize=20)

plt.show()