'''
Created on 10/06/2013

@author: Pablo
'''
class Disk:
    def __init__(self):
        self.listOfProgram = {}
        
    def load(self, aProgram):
        self.listOfProgram[aProgram.getName()] = aProgram
    
    def get(self, aNameOfProgram):
        return self.listOfProgram[aNameOfProgram]
    
    def isInDisk(self, aNameOfProgram):
        #=======================================================================
        # result = False
        # for prog in self.listOfProgram:
        #     if prog.getName() == aNameOfProgram:
        #         result = True
        #         break
        #=======================================================================
        if aNameOfProgram in self.listOfProgram:
            return True
        else:
            return False
        

            