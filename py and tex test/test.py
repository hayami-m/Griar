import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
#style.use('seaborn-ticks')

def k(s, p):
    return prob(s, p)/len(node)

def prob(s, p):
    if len(node[s[0]]) == 0:
        return 0
    if len(s) == 1 :
        return p
    m = len (s)
    S =(1-p) / len(node[s[0]])* prob(s[1:m], p)    
    return S

node = [[] for _ in range(5)]
node[0]= [2,4]; node[1]=[4]; node[2]=[1,5]
node[3]=[1,5]; node[4] =[3]
print(k([0,3,2,4,2],1/3))