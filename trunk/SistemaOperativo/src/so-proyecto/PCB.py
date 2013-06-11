'''
@author: Pablo
'''

class PCB:
#Process Control Block
    def __init__(self,aProgramm, aPid , aPriority=10, aPC):
        self.id = aProgramm
        self.pid = aPid
        self.status
        self.priority = aPriority
        self.pc = aPC
        self.dirBase = None
    
    def changeStatus(self, aNewStatus):
        self.status=aNewStatus
        
    def increasePc(self):
        self.pc+=1
        
    def decreasePriority(self):
        self.priority = self.priority - 1
        
    def getSize(self):
        return self.id.getSize()
    
    def setDirBase(self, aDirection):
        self.dirBase= aDirection   
        
    def getInstruction(self):
        return self.id.getInstruction()
    
    