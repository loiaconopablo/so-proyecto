'''
Created on 30/05/2013

@author: Pablo Loiacono
'''
import abc
from Block import *
from PCB import *

class MemPolicity:
    
    __metaclass__ = abc.ABCMeta  # la define como claseAbstracta
                          
    @abc.abstractclassmethod
    def choiseBlock(self, aFreeListBlock, sizePCB):
        pass
    
    def isFreeBlockTo(self, aFreeListBlock, aSize):
        result = False
        for block in aFreeListBlock:
            if block.getSize() >= aSize:
                result = True
                break
        return result
    
    def savePCB(self, aFreeListBlock, aPCB):
        sizePCB = aPCB.getSize()
        bestBlock = self.choiseBlock(aFreeListBlock, sizePCB)  # Aca va a lógica de cada Policitica                         
        aPCB.setDirBase(bestBlock.getDirBase())  # Seteo en el pcb en que celda se guarda en memoria
        position = aFreeListBlock.index(bestBlock)  # Tengo que pedirle el indice a la lista del objeto
        bestBlock.pcbAssociated = aPCB  # AGREGO AL BLOQUE DONDE SE GUARDA EL PCB, ESTE MISMO.
        if self.quedanCeldasVacias(bestBlock, sizePCB):  # Pregunto si quedan celdas que no se usen
            self.resizeBlock(aFreeListBlock, sizePCB, bestBlock)        
        return aFreeListBlock.pop(position)
 
    def quedanCeldasVacias(self, block, sizeInstruction): 
        return block.getSize() != sizeInstruction          

    def resizeBlock(self, aFreeListBlock, sizePCB, bestBlock):
        newFreeBlock = Block((bestBlock.getDirBase() + sizePCB), bestBlock.getdDirEnd())  # Genero nuevo bloque vacio de la sobra
        aFreeListBlock.append(newFreeBlock)  # Agrego el bloque vacio a la lista de los vacios.
        bestBlock.dirEnd = (bestBlock.getDirBase() + sizePCB) - 1  # Recorto al bloque asignado
        
#-----------------------------------------------------         
class PrimerAjuste(MemPolicity):
    
    def __init__(self):
        self
     
    def choiseBlock(self, aFreeListBlock, sizePCB):
        bestBlock = None
        for block in aFreeListBlock:
            if block.getSize() >= sizePCB:
                bestBlock = block
                break
        return bestBlock

#-----------------------------------------------------    

class MejorAjuste(MemPolicity):
    
    def __init__(self):
        self       

    def choiseBlock(self, aFreeListBlock, sizePCB):
        bestBlock = None
        garbage = 31
        for block in aFreeListBlock:
            if (block.getSize() >= sizePCB) and (garbage > (block.getSize()) - sizePCB):  # pregunta si entra y si tiene un menor desperdicio
                bestBlock = block
                garbage = sizePCB - block.getSize()
        return bestBlock

#-----------------------------------------------------    

class PeorAjuste(MemPolicity):
    
    def __init__(self):
        self
    
    def choiseBlock(self, aFreeListBlock, sizePCB):
        bestBlock = None
        garbage = 0
        for block in aFreeListBlock:
            if (block.getSize() >= sizePCB) and (garbage < (block.getSize()) - sizePCB):  # pregunta si entra y si tiene un mayor desperdicio
                bestBlock = block
                garbage = sizePCB - block.getSize()
        return bestBlock
        
