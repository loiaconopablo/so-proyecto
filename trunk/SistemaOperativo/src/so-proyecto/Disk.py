'''
Created on 10/06/2013

@author: Pablo
'''
class Disk:
    def __init__(self):
        self.listOfProgram = {}
        
    def load(self,aNameProgram, aProgram):
        self.listOfProgram[aNameProgram] = aProgram
    
    def get(self, aNameOfProgram):
        return self.listOfProgram[aNameOfProgram]
        