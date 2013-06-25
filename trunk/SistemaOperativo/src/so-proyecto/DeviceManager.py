'''
Created on 15/06/2013

@author: Pablo
'''
from PCB import *
from Device import *



class DeviceManager:
    def __init__(self, aManageIRQ):
        self.devices = {}
        self.manageIRQ = aManageIRQ
        
    def get(self, aDevice):
        return self.devices[aDevice]
    
    def handle(self, aDevice , aPCB, nextInstruccion):
        device = self.get(aDevice)
        device.addTask(aPCB, nextInstruccion)

    def addDevice(self, aDeviceName):
         self.devices[aDeviceName] = aDeviceName(self)

    def initializeThread(self): #Verificar si esta bien el for para recorrer el dictionary
        for i in self.devices:
            i.start()
            
    def downThread(self):
        self #ver como dar de bajas los thread