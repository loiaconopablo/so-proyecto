'''
Created on 30/05/2013

@author: Pablo Loiacono
'''
import abc

class MemPolicitity:
    
    __metaclass__ = ABCMeta  # la define como claseAbstracta
     
    @abc.abstractclassmethod
    def savePCB(self, aFreeListBlock, aPCB):
        self                            
    
    def isFreeBlockTo(self, aFreeListBlock, aSize): # preguntar si al heredar lo utilizan
        for block in aFreeListBlock:
            if block.getSize() >= aSize:
                result = True
                break
            else: result = False
        return result
    
    def quedanCeldasVacias(self, block, sizeInstruction): 
       return block.getSize() != sizeInstruction          
   
 #-----------------------------------------------------         
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
                
                if self.quedanCeldasVacias(block, sizePCB):
                    newFreeBlock = Block((block.getDirBase()+sizePCB),block.getdDirEnd()) # genero nuevo bloque vacio de la sobra
                    aFreeListBlock.append(newFreeBlock)
                    block.dirEnd=((block.getDirBase()+sizePCB)-1) # recorto al bloque asignado
                
                return aFreeListBlock.pop(position) #retorno al bloque usado y lo saco de la lista de free
                break     


#-----------------------------------------------------    
class MejorAjuste(MemPolicitity):
    
    def __init__(self):
        self
        
    def savePCB(self, aFreeListBlock, aPCB):
        sizePCB = aPCB.getSize()
        bestBlock = null
        garbage = 17
        for block in aFreeListBlock:
            if (block.getSize() >= sizePCB) and (garbage<(block.getSize()) - sizePCB): #pregunta si entra y si tiene un menor desperdicio
                bestBlock = block
                garbage= sizePCB - block.getSize()                     
                
        aPCB.setDirBase(bestBlock.getDirBase())
        position = aFreeListBlock.index(bestBlock)  # tengo que pedirle el indice a la lista del objeto
        bestBlock.pcbAssociated = aPCB  # AGREGO AL BLOQUE DONDE SE GUARDA EL PCB, ESTE MISMO.
                
        if self.quedanCeldasVacias(bestBlock, sizePCB):
            newFreeBlock = Block((bestBlock.getDirBase()+sizePCB),bestBlock.getdDirEnd()) # genero nuevo bloque vacio de la sobra
            aFreeListBlock.append(newFreeBlock)
            bestBlock.dirEnd=((bestBlock.getDirBase()+sizePCB)-1) # recorto al bloque asignado
                
        return aFreeListBlock.pop(position) #retorno al bloque usado y lo saco de la lista de free   
