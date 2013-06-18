'''
Created on 10/06/2013

@author: Pablo
'''
class IOInstruccion:
        def __init__(self, aAction, aDeviceName):
                self.action = aAction  # Un String que diga algo para saber que se ejecuto
                self.deviceName = aDeviceName
                
        def execute(self, aMemory):
             print(self.action)
                
        def getDeviceName(self):
            return self.deviceName
        
        def isIO(self):
            return True
             
