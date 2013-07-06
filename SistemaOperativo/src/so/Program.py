'''
@author: Pablo
'''

class Program:
        def __init__(self, aName):
                self.instruction = []
                self.programName = aName
                self.memory = False
        
        def add(self, aObject):
                self.instruction.append(aObject)
            
        def getSize(self):
            return len(self.instruction)
        
        def isInMemory(self):
            return self.memory
        
        def loadInMemory(self):
            self.memory = True
            
        def outMemory(self):
            self.memory = False
            
        def getName(self):
            return self.programName
            
            
            
