'''
@author: Pablo
'''

class PCB:
#Process Control Block
    def __init__(self,aProgramm, aPid , aPriority=1, aPC):
        self.id = aProgramm
        self.pid = aPid
        self.status
        self.priority = aPriority
        self.pc = aPC
    
    def changeStatus(self, aNewStatus):
        self.status=aNewStatus
        
    def increasePc(self):
        self.pc+=1
        
    
    