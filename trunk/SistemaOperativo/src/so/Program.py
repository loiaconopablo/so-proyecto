'''
@author: Pablo
'''

class Program:
        def __init__(self, aName, priority=10):
                self.instruction = []
                self.programName = aName
                self.memory = False
                self.priority = priority #Si no se le pasa prioridad se carga por defecto 10
        
        def add(self, instruccion):
                self.instruction.append(instruccion)
            
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
            
        def getInstruction(self):
            return self.instruction
            
            
