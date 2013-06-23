'''
Created on 10/06/2013

@author: Pablo
'''
from PCB import *
from IOInstruccion import *

class HandlerIO:  # preguntar si tiene que ser otro Thread mas, - Me dijo Marce que no es necesario, que lo pruebe igual.
    def __init__(self, aDeviceMange):
        self.deviceManage = aDeviceManage
            
    def handleIO(self, aPCB , nextInstruccion):
        aPCB.changeStatus(State.WAITING)
        device = self.nextInstruccion.getDeviceName()
        self.deviceManage.handle(device, aPCB, nextInstruccion)
        
    
