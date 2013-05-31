'''
Created on 27/05/2013

@author: Pablo
'''
from MemPolicity import *
 
class Memory:
    
    def __init__(self, aMemPolicity):
        self.physicalMemory = {x: None for x in range(1, 1025)}  # Devuelve un dictionary con 1024 celdas vacias
        #=======================================================================
        # a= {x: None for x in range(1,1025)}
        # print (a)  
        #         El resultado que da es: {1: None, 2: None, 3: None,.... 1023: None, 1024: None}
        #=======================================================================
        self.blocks = [Block(1,1024)]  # memoria logica, tiene un solo bloque al principio
        self.freeBlocks = [Block(1,1024)]  # memoria logica, tiene un bloque entero libre
        self.policityMemory = aMemPolicity
    
    def sizeMemory(self):
        return len(self.physicalMemory)
    
    def freeCellsize (self):
        contador = 0
        for block in self.freeBlocks: 
         contador = contador + block.getSize()
        return contador 
    
    def saveInMemory(self, aPCB):
        if self.freeCellsize() > aPCB.size():
            if self.isFreeBlockTo(aPCB):
                self.assignBlock(aPCB) 
            else:
                self.compact(aPCB.getSize())  # Se le dice Compacta y se le pasa el tamaño que se necesista, asi compacta 
                self.assignBlock(aPCB)  # hasta llegar al tamaño que se necesita y para
        else:
            self.longScheduler.push(aPCb) # ****************IMPLENTAAR******************
            
    def assignBlock(self, aPCB):
        # agregado Logico
        blockUse = self.policityMemory.savePCB(self.freeBlocks, aPCB)  # extrae bloque libre segun politica, lo saca de la lista de free y asigna pcb     
        self.addBlock(blockUse)  # agrega el bloque "usado" con el pcb a la lista de bloques
        
        # agregado Fisico
        self.addInstruction(blockUse.getDirBase(), aPCB.getInstruction())
        
    def addInstruction(self, aDirBase, aListInstruction):
        dirBaseMem = aDirBase
        for i in aListInstruction:
            self.physicalMemory[dirBaseMem] = i
            dirBaseMem = dirBaseMem + 1
            
    def isFreeBlockTo(self, aPCB):
        return self.policityMemory.isFreeBlockTo(self.freeBlocks, aPCB.getSize())
    
    def giveMeFreeBlockFromCell(self, aDirCell):
        for block in self.freeBlocks:
            if block.containDir(aDirCell):
                return (self.freeBlocks.pop(block))
                break
        
    def compact(self):
        self  # IMPLEMENTAR
        
    def releaseMemory(self, baseCell, endCell):
        self  # IMPLEMENTAR
        
