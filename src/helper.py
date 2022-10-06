import numpy as np
import math
import random
from functools import reduce

NUMBER_OF_CHALLENGES=10000

def Xor(a,b):
    return a^b

def getBinaryVector(length):
    binaryVector=[]
    for i in range(length):
        binaryVector.append(random.randint(0,1))
    return binaryVector

def scalarProduct(a,s):
    l=[]
    for i in range(len(a)):
        l.append(a[i]*s[i])
    product=reduce(Xor,l)
    return product

def BernouliNoise(p):
    x=np.random.binomial(1,p)
    return x