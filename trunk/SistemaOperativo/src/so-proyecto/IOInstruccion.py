'''
Created on 10/06/2013

@author: Pablo
'''
class IOInstruccion:
        def __init__(self, aAction, IO , aDevice ):
                self.action = aAction #Un String que diga algo para saber que se ejecuto
                self.isIO = IO # Tiene que ser un bool que indique si es 
                self.device = aDevice
                
        def execute(self, aMemory):
             print(self.action)
                
        def getDevice(self):
            return self.device