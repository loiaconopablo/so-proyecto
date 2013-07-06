'''
@author: Pablo
'''
class Instruccion:
        def __init__(self, aAction):
                self.action = aAction #Un String que diga algo para saber que se ejecuto
                
        def execute(self, aMemory):
            print(self.action)
             
        def isIO(self):
            return False
             
        
                
