from src.lock import *

if __name__=="__main__":
    card=Card()
    lock=Lock()
    p=0.3
    length=1000
    key=getBinaryVector(length)
    card.addData(key,p)
    lock.addData(key,p)
    print(lock.unlock(card))