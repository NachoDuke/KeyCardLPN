from src.card import *


class Lock():
    def __init__(self):
        self.numChallenges=NUMBER_OF_CHALLENGES
        self.length=0
        self.p=0
        self.key=[]
    
    def addData(self,key,p):
        self.key=key
        self.length=len(self.key)
        self.p=p
    
    def compute(self,binaryVector):
        result=scalarProduct(binaryVector,self.key)
        return result

    def challenge(self,keycard):
        binaryVector=getBinaryVector(self.length)
        if(keycard.query(binaryVector)==self.compute(binaryVector)):
            return True
        else:
            return False

    def unlock(self,keycard):
        count=0
        for i in range(self.numChallenges):
            if(self.challenge(keycard)):
                count+=1
        fraction=count/self.numChallenges
        print(fraction)
        if(math.fabs(1-fraction-self.p)<=0.01):
            return True
        else:
            return False
