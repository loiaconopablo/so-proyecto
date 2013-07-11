'''
@author: Pablo
'''
from State import *
from Program import *
import uuid

class PCB:
#Process Control Block
    def __init__(self,aProgramName):
        self.id = None
        self.aProgramName=aProgramName
        self.pid = uuid.uuid4() # Genera un número - Generate a random UUID
        self.status= State.NEW
        self.dirBase = None
        self.pc = 0
        self.priority = 0 # Luego se le carga la prioridad del programa, una vez que se carga
    
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
    
    def getNameProgram(self):
        return self.aProgramName
    
    def setPriority(self, aPriority):
        self.priority = aPriority
    
    def setProgram(self, aProgram):
        self.id = aProgram
        
    def getInstruction(self):
        return self.id.getInstruction()