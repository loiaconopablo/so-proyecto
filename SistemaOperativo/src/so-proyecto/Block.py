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

    def cellDestino(self):
        return self.dirFin+1
        
        
    
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