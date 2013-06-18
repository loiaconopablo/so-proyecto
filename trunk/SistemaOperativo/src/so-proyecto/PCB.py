'''
@author: Pablo
'''
from State import *

class PCB:
#Process Control Block
    def __init__(self,aProgramm, aPid, aPriority=10):
        self.id = aProgramm
        self.pid = aPid
        self.status= State.NEW
        self.dirBase = None
        self.pc = 0
        self.priority = aPriority
    
    def changeStatus(self, aNewStatus):
        self.status=aNewStatus
        
    def increasePc(self):
        self.pc+=1
        
    def decreasePriority(self):
        self.priority = self.priority - 1
        
    def getSize(self):
        return self.id.getSize()
    
    def setDirBase(self, aDirection):
        self.dirBase= aDirection   
    
    def nextDirInstruccion(self):
        return self.dirBase+self.pc
    
    def isProgramInMemory(self):
        return self.id.isInMemory()
    
    def runInstruccion(self):
        self.status=State.RUNNING
        return self.id.runInstruccion(self.nextDirInstruccion())
