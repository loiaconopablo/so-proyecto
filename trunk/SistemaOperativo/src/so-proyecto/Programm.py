'''
@author: Pablo
'''

class Programm:
        def __init__(self):
                self.instruction = []
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
            
            
            