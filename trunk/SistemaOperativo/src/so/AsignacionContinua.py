'''
Created on 27/05/2013

@author: Pablo
'''
from Block import *
 
class AsignacionContinua:
    
    def __init__(self, aMemPolicity, aMMU):
        self.MMU = aMMU
        self.busyBlock = []  # memoria logica, no tiene bloques usados al principio al principio
        self.freeBlocks = [Block(1, 32)]  # memoria logica, tiene un bloque entero libre
        self.policityMemory = aMemPolicity

    def freeSize (self):
        contador = 0
        for block in self.freeBlocks:  
            contador = contador + block.getSize()
        return contador 
    
    def saveInMemory(self, aPCB):
            if self.isFreeBlockTo(aPCB):
                self.assignBlock(aPCB)
            else:
                self.compact()  # Se le dice Compacta 
                self.assignBlock(aPCB)
                
    def assignBlock(self, aPCB):
        # Agregado Logico
        blockUse = self.policityMemory.savePCB(self.freeBlocks, aPCB)  # extrae bloque libre segun politica, lo saca de la lista de free y asigna pcb     
        self.addBlock(blockUse)  # agrega el bloque "usado" con el pcb a la lista de bloques
        self.MMU.addToPhysicalMem(blockUse.getDirBase(), aPCB.getInstruction()) # agregado Fisico
            
    def addBlock(self, aBlock):
        self.busyBlock.append(aBlock)
        
    def isFreeBlockTo(self, aPCB):
        return self.policityMemory.isFreeBlockTo(self.freeBlocks, aPCB.getSize())

    def compact(self):  # COMPACTA TODA LA MEMORIA
        self.orderBlocks(self.busyBlock) #Ordenar Bloques Usados por direccion de base
        freeDir = self.firstFreeCell() #Obtengo primera celda libre
        for block in self.busyBlock:       
            if block.dirBase > freeDir: # Pregunto si el bloque esta despues de la celda libre
                freeDir = self.moveBlockTo(freeDir, block)
        self.compactFreeCell(freeDir) #Creo un bloque libre grande
    
    def moveBlockTo(self, freeDir, block):
        oldCellRange = range(block.dirBase, (block.dirEnd + 1)) #Guardo la ubicacion vieja
        blockSize = block.getSize() # guardo el tamaño del bloque = la cantidad de instrucciones
        block.dirBase = freeDir #Seteo la nueva direccion inicial
        block.pcbAssociated.setDirBase(freeDir) # MODIFICO AL PCB ASOCIADO AL BLOQUE, SU DIRECCION  DE INICIO.
        block.dirEnd = block.dirBase + (blockSize - 1) #Seteo la nueva direccion final
        newCellRange = range(block.dirBase, (block.dirEnd + 1)) #Guardo la ubicacion nueva
        freeDir = block.dirEnd + 1
        self.MMU.moveInfoPhysicalMem(oldCellRange, newCellRange)
        return freeDir
        
    def compactFreeCell(self,freeDir):#  COMPACTANDO BLOQUES SIN USO
        # positionLastBlock = ((len(self.busyBlock)) - 1 )  # ME GUARDO LA POSICION DEL ULTIMO BLOQUE
        # lastBlock = self.busyBlock[positionLastBlock]  # ME GUARDO AL ULTIMO BLOQUE.
        self.freeBlocks = [Block((freeDir), 32)]  # CREO EL BLOQUE LIBRE QUE SALIO DE COMPACTAR.

    def orderBlocks(self, aListOfBlocks):
        aListOfBlocks.sorted(self.queue, key = lambda block: block.dirBase) #ordenado por la direccion base
        
    def firstFreeCell(self):
        firstCell = self.freeBlocks[0].dirBase  # guarda la primera cell del primer bloque libre, para tener un valor de referencia
        for block in self.freeBlocks:  # compara las direcciones de celdas, si el menor la guarda
            if block.dirBase < firstCell:
                firstCell=block.dirBase
        return firstCell

    def release(self, aPCB):
        block = self.giveMeFreeBlockFromCell(aPCB.dirBase)
        self.MMU.releaseMemory(block.dirBase, block.dirEnd) #borra la memoria fisica
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

        
        
        
