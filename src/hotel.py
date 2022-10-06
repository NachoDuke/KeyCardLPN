from re import A
from src.lock import *

class Hotel():
    def __init__(self,n,length):
        self.numRooms=n
        self.rooms=[]
        self.keys=[]
        self.booked=[]
        self.l=length
        for i in range(self.numRooms):
            a=random.random()
            self.rooms.append(Lock())
            self.rooms[i].addData(getBinaryVector(self.l),a)
            self.keys.append(Card())
            self.keys[i].addData(getBinaryVector(self.l),a)
            self.booked[i]=False

    def open(self,roomNo,keyNo):
        if(self.rooms[roomNo].unlock(self.keys[keyNo])):
            print("Success")
        else:
            print("Failure")

    