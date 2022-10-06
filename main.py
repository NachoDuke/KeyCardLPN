from src.lock import *

if __name__=="__main__":
    card=Card()
    lock=Lock()
    numKeys=50
    p=0.3
    length=1000
    keys=[]
    for i in range(numKeys):
        keys.append(getBinaryVector(length))
    card.addData(keys[0],p)
    count=0
    for i in range(numKeys):
        lock.addData(keys[i],p)
        if(lock.unlock(card)):
            count+=1
    print(count)