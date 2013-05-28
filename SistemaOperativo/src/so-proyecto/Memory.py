'''
Created on 27/05/2013

@author: Pablo
'''
class Memory:
    
    def __init__(self, aMemPolicity):
        self.physicalMemory={1024}
        self.blocks = []
        self.freeBlocks = []
        self.policityMemory= aMemPolicity()
    
    def sizeMemory(self):
        return len(self.physicalMemory)
    
    def freeCellsize (self):
        contador = 0
        for block in self.freeBlocks: 
         contador = contador + block.getSize()
        return contador 
    
    def saveInMemory(self, aPCB):
        if self.freeCellsize()>aPCB.size():
            if self.isFreeRoomTo(aPCB):
                self.assignBlock(aPCB) 
            else:
                self.compact()
                self.assignBlock(aPCB)
        else:
            longScheduler.push(aPCb)
            
    def assignBlock(self, aPCB):
        blockUse = self.aMemPolicity.savePCB(self.freeBlocks, aPCB) #usa el bloque libre segun politica, lo saca de la lista de free y asigna pcb
        self.addInstruction(blockUse.getDirBase(), aPCB.getInstruction())
        self.addBlock(blockUse) #agrega el bloque "usado" con el pcb a la lista de bloques
        
    def addInstruction(self, aDirBase, aListInstruction):
        dirBaseMem = aDirBase
        for i in aListInstruction:
            self.physicalMemory[dirBaseMem]= i
            dirBaseMem = dirBaseMem +1
            
    def isFreeRoomTo(self, aPCB):
        return self.policityMemory.isFreeRoomTo(self.freeBlocks, aPCB)
    
    
    #def compact(self):
        
    def releaseMemory(self, baseCell, endCell):
        