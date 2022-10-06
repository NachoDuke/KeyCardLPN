from src.helper import *

class Card():
    def __init__(self):
        self.length=0
        self.key=[]
        self.p=0
    
    def query(self,a):
        result=scalarProduct(a,self.key)
        x=BernouliNoise(self.p)
        return Xor(x,result)
    
    def addData(self,key,p):
        self.key=key
        self.p=p
        self.length=len(key)