'''
Created on 09/07/2013

@author: Pablo Loiacono
'''
class MMU:
    def __init__(self):
        self.logicalMemory = None
        self.physicalMemory = {x: None for x in range(1, 33)}  # Devuelve un dictionary con 32 celdas vacias
        
    def read(self, cell):
        return self.physicalMemory[cell]
        
    def saveInMemory(self, aPCB):
        self.logicalMemory.saveInMemory(aPCB)
        
    def sizeMemory(self):
        return len(self.physicalMemory)
    
    def freeSize(self):
        return self.logicalMemory.freeSize()
        
    def addToPhysicalMem(self, aDirBase, aListInstruction):
        dirBaseMem = aDirBase
        for i in aListInstruction:
            self.physicalMemory[dirBaseMem] = i
            dirBaseMem = dirBaseMem + 1
    
    def moveInfoPhysicalMem(self, oldCellRange, newCellRange):
        for a, b in zip(oldCellRange, newCellRange):
            info = self.physicalMemory[a]
            self.physicalMemory[b] = info #Copia el contenido
            self.physicalMemory[a] = None #Libera la celda
    #De donde saque la info: http://stackoverflow.com/questions/2672936/multiple-counters-in-a-single-for-loop-python
        
    def release(self, aPCB):
        self.logicalMemory.release(aPCB)
    
    def releaseMemory(self, baseCell, endCell):         
        for i in range(baseCell,(endCell +1)):
            self.physicalMemory[i] = None
        
    def setLogicalMemory(self, aTypeOfLogicalMem):
        self.logicalMemory = aTypeOfLogicalMem