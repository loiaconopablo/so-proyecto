'''
@author: Pablo
'''

class Programm:
        def __init__(self,aMemory):
                self.instruction = []
                self.memory = aMemory
        
        def add(self, aObject):
                self.instruction.append(aObject)

        def run(self):
                for i in self.instruction:
                        i.execute(self.memory)

        def getSize(self):
            return len(self.instruction)
        
        def getInstruction(self):
            return self.instruction