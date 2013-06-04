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
    
    # HACE FALTA EL GIVEMEFREEBLOCKFROMCELL???!!!!!  PARA QUE??!!!
    def giveMeFreeBlockFromCell(self, aDirCell):
        for block in self.freeBlocks:
            if block.containDir(aDirCell):
                return (self.freeBlocks.pop(block))
                break
    # HACE FALTA EL GIVEMEFREEBLOCKFROMCELL???!!!!!  PARA QUE??!!!
        
    def compact(self): # COMPACTA TODA LA MEMORIA
        self.compactLogicMemory()
        self.compactPhysicalMemory()
        
    def compactLogicMemory(self):
        
        #  COMPACTANDO BLOQUES EN USO
        lastDir = self.firstFreeDir()
        for block in self.blocks:
            blockSize = block.getSize() # guardo el tamaño del bloque = la cantidad de instrucciones
            block.dirBase = lastDir  # SETTEO LA DIRBASE DEL BLOQUE
            block.pcbAssociated.setDirBase(lastDir) # MODIFICO AL PCB ASOCIADO AL BLOQUE, SU DIRECCION  DE INICIO.
            block.dirEnd = block.dirBase + (block.getSize() - 1)
            lastDir = block.dirEnd + 1    
        
        #  COMPACTANDO BLOQUES SIN USO
        positionLastBlock = (len(self.blocks)) - 1 # ME GUARDO LA POSICION DEL ULTIMO BLOQUE
        lastBlock = self.blocks[positionLastBlock] # ME GUARDO AL ULTIMO BLOQUE.
        self.freeBlocks = [Block((lastBlock.dirEnd() + 1), 1024)] # CREO EL BLOQUE LIBRE QUE SALIO DE COMPACTAR.
        
    def firstFreeDir(self):
        firstCell = self.freeBlocks(0).dirBase #guarda la primera cell del primer bloque libre, para tener un valor de referencia
        for block in self.freeBlocks: #compara las direcciones de celdas, si el menor la guarda
            if block.dirBase<firstCell:
                firstCell=block.dirBase
        
        return firstCell
            
        
    def compactPhysicalMemory(self):
        for block in self.blocks:
            self.addInstruction(block.getDirBase(), block.pcbAssociated.getInstruction())
        
        
    #===========================================================================
    # def releaseMemory(self, baseCell, endCell):
    #     
    #     for i in range(baseCell,(endCell +1)):
    #         self.physicalMemory[i] = None
    #===========================================================================
    # PARA QUE SERVIRIA? 
    # Rta: Sirver para liberar memoria fisica de un sector.
        
        
    def addBlock(self, aBlock):
        # IMPLEMENTAR -> agregar el bloqueParametro a la lista de bloques usados
        self.blocks.append(aBlock)
        
