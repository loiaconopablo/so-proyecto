'''
Created on 27/05/2013

@author: Pablo
'''
class Block:

    def __init__(self,baseCell,endCell):
        self.dirBase=baseCell
        self.dirEnd=endCell
         #self.inMemory=False

    def setPid(self,process):
        self.pid=process
    
    def getDirBase(self):
        return self.dirBase

    def getSize(self):
        return (self.dirEnd - self.dirBase)

    def setDirBase(self,direction):
        self.dirBase=direction
        
    def getDirEnd(self):
        return self.dirEnd
        
    def cellDestino(self):
        if not self.lastCell():
            return (self.dirFin+1)
        else: 
            return None
    
    def cellAnterior(self):
        if not self.firstCell():
            return (self.dirBase-1)
        else: 
            return None
        
    def lastCell(self):
        return (self.dirBase==0)
    
    def firstCell(self):
        return (self.dirEnd==1024)
             
    def containDir(self, aDirCell): #pregunta si una direccion esta incluida en el bloque
       # return (aDirCell in range(self.getDirBase(),self.getDirEnd()+1)) Otra Opcion de hacerlo
        return (self.getDirBase()>= aDirCell and self.getDirEnd()<= aDirCell)
    
    #===========================================================================
    # def getInMemory(self):
    #       return self.inMemory
    #
    # def inMemoryOn(self):
    #     self.inMemory = True
    # 
    # def inMemoryOff(self):
    #     self.inMemory = False    
    #===========================================================================