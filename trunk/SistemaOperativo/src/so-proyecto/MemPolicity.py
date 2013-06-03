'''
Created on 30/05/2013

@author: Pablo Loiacono
'''
from abc import ABCMeta

class MemPolicitity:
    
    __metaclass__ = ABCMeta  # la define como claseAbstracta
     
    @abstractmethod
    def savePCB(self, aFreeListBlock, aPCB):
        self                            
    
    @abstractmethod   
    def isFreeBlockTo():
        self

class PrimerAjuste(MemPolicitity):
    
    def __init__(self):
        self
            
    def savePCB(self, aFreeListBlock, aPCB):
        sizePCB = aPCB.getSize()
        for block in aFreeListBlock:
            if block.getSize() >= sizePCB:
                aPCB.setDirBase(block.getDirBase())
                position = aFreeListBlock.index(block)  # tengo que pedirle el indice a la lista del objeto
                block.pcbAssociated = aPCB  # AGREGO AL BLOQUE DONDE SE GUARDA EL PCB, ESTE MISMO.
                
                if self.quedaCeldasVacias(block, sizePCB):
                    newFreeBlock = Block((block.getDirBase()+sizePCB),block.getdDirEnd()) # genero nuevo bloque vacio de la sobra
                    aFreeListBlock.append(newFreeBlock)
                    block.dirEnd=((block.getDirBase()+sizePCB)-1) # recorto al bloque asignado
                
                return aFreeListBlock.pop(position) #retorno al bloque usado y lo saco de la lista de free
                break
        
    def quedanCeldasVacias(self, block, sizeInstruction): 
       return block.getSize() != sizeInstruction
                
               
        
    def isFreeBlockTo(self, aFreeListBlock, aSize):
        for block in aFreeListBlock:
            if block.getSize() >= aSize:
                result = True
                break
            else: result = False
        return result
                
        
