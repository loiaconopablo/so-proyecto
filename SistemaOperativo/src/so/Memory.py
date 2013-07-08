'''
Created on 27/05/2013

@author: Pablo
'''
from MemPolicity import *
from Block import *
from PCB import *
 
class Memory:
    
    def __init__(self, aMemPolicity):
        self.physicalMemory = {x: None for x in range(1, 33)}  # Devuelve un dictionary con 32 celdas vacias
        #=======================================================================
        # a= {x: None for x in range(1,32)}
        # print (a)  
        #         El resultado que da es: {1: None, 2: None, 3: None,.... 31: None, 32: None}
        #=======================================================================
        self.busyBlock = []  # memoria logica, no tiene bloques usados al principio al principio
        self.freeBlocks = [Block(1, 16)]  # memoria logica, tiene un bloque entero libre
        self.policityMemory = aMemPolicity
    
    def sizeMemory(self):
        return len(self.physicalMemory)

    def freeSize (self):
        contador = 0
        for block in self.freeBlocks:  
            contador = contador + block.getSize()
        return contador 
    
    def saveInMemory(self, aPCB):
            if self.isFreeBlockTo(aPCB):
                self.assignBlock(aPCB)
            else:
                self.compact(aPCB.getSize())  # Se le dice Compacta y se le pasa el tamaño que se necesista, asi compacta 
                self.assignBlock(aPCB)  # hasta llegar al tamaño que se necesita y para
            
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
            
    def addBlock(self, aBlock):
        self.busyBlock.append(aBlock)
        
    def isFreeBlockTo(self, aPCB):
        return self.policityMemory.isFreeBlockTo(self.freeBlocks, aPCB.getSize())
    
    #===========================================================================
    # def getAllBlocks(self):
    #     newlist= self.busyBlock.append(self.freeBlocks)
    #     newlist.sorted(self.queue, key = lambda block: block.dirBase) #ordenado por la direccion base
    #     return newlist
    #===========================================================================
        
    def compact(self):  # COMPACTA TODA LA MEMORIA
        #POner en modo Kernel primero
        self.orderBlocks(self.busyBlock)
        if self.busyBlock[0].dirBase == 1:
            for block in self.busyBlock
        
        
    def compactLogicMemory(self):
        #  COMPACTANDO BLOQUES EN USO
        firstFree = self.firstFreeBlock()
        for block in self.busyBlock:
            blockSize = block.getSize()  # guardo el tamaño del bloque = la cantidad de instrucciones
            block.dirBase = firstFree  # SETTEO LA DIRBASE DEL BLOQUE
            block.pcbAssociated.setDirBase(firstFree)  # MODIFICO AL PCB ASOCIADO AL BLOQUE, SU DIRECCION  DE INICIO.
            block.dirEnd = block.dirBase + (block.getSize() - 1)
            firstFree = block.dirEnd + 1    
      
        #  COMPACTANDO BLOQUES SIN USO
        positionLastBlock = (len(self.busyBlock)) - 1  # ME GUARDO LA POSICION DEL ULTIMO BLOQUE
        lastBlock = self.busyBlock[positionLastBlock]  # ME GUARDO AL ULTIMO BLOQUE.
        self.freeBlocks = [Block((lastBlock.dirEnd() + 1), 32)]  # CREO EL BLOQUE LIBRE QUE SALIO DE COMPACTAR.
    def compactPhysicalMemory(self):
        for block in self.busyBlock:
            self.addInstruction(block.getDirBase(), block.pcbAssociated.getInstruction())
        
    def orderBlocks(self, aListOfBlocks):
        aListOfBlocks.sorted(self.queue, key = lambda block: block.dirBase) #ordenado por la direccion base
        
    def firstFreeBlock(self):
        firstCell = self.freeBlocks(0).dirBase  # guarda la primera cell del primer bloque libre, para tener un valor de referencia
        for block in self.freeBlocks:  # compara las direcciones de celdas, si el menor la guarda
            if block.dirBase < firstCell:
                firsFreeBlock=block
        return firsFreeBlock

    def release(self, aPCB):
        block = self.giveMeFreeBlockFromCell(aPCB.dirBase)
        self.releaseMemory(block.dirBase, block.dirEnd) #borra la memoria fisica
        block.pcbAssociated = None #libera el bloque
        position = self.busyBlock.index(block)
        self.freeBlocks.append(self.busyBlock.pop(position)) #saca el bloque de la lista de free y lo agrega a la otra lista       
            
    #estos metodos son para el release
    def giveMeFreeBlockFromCell(self, aDirCell):
        for block in self.busyBlock:
            if block.containDir(aDirCell):
                position= self.busyBlock.index(block)
                return (self.busyBlock[position])
                break
    
    def releaseMemory(self, baseCell, endCell):         
        for i in range(baseCell,(endCell +1)):
            self.physicalMemory[i] = None
   
        
        
        
        
