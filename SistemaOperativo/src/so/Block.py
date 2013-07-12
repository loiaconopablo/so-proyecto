'''
Created on 27/05/2013

@author: Pablo
'''
class Block:

    def __init__(self, baseCell, endCell):
        self.dirBase = baseCell
        self.dirEnd = endCell
        self.pcbAssociated = None
    
    def getDirBase(self):
        return self.dirBase

    def getSize(self):
        return ((self.dirEnd - self.dirBase) + 1)

    def setDirBase(self, direction):
        self.dirBase = direction
        
    def getDirEnd(self):
        return self.dirEnd
             
    def containDir(self, aDirCell):  # pregunta si una direccion esta incluida en el bloque
        #return (self.getDirBase() >= aDirCell and self.getDirEnd() <= aDirCell)
        return (aDirCell in range(self.getDirBase(),self.getDirEnd()+1)) #Otra Opcion de hacerlo
    
    def isInUse(self):
        return (self.pcbAssociated!=None)
