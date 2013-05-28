'''
Created on 27/05/2013

@author: Pablo
'''

class MemPolicitityPrimerAjuste:
    
    def __init__(self):
        self
            
    def savePCB(self, aFreeListBlock, aPCB):
        sizePCB = aPCB.getSize()
        for i in aFreeListBlock:
            if i.getSize() >= sizePCB:
                aPCB.setDirBase(i.getDirBase())
                return aFreeListBlock.pop(i)
                break
        
        
    #def isFreeRoomTo():
