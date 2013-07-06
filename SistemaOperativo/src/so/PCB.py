'''
@author: Pablo
'''
from State import *
from Program.py import *
import uuid

class PCB:
#Process Control Block
    def __init__(self,aProgramName, aPriority=10):
        self.id = aProgramName
        self.pid = uuid.uuid4() # Genera un número - Generate a random UUID
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
    
    def isLastInstruccion(self):
        return (self.pc == self.getSize())
    
    def getNameProgram(self): # por ahora no se usa
        return self.id.getName()
    
    def setProgram(self, aProgram):
        self.id = aProgram