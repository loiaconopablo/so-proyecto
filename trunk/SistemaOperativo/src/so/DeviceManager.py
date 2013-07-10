'''
Created on 15/06/2013

@author: Pablo
'''
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

    def addDevice(self, aDevice):
        aDevice.setManager(self)
        self.devices[aDevice.getName()] = aDevice

    def initializeThread(self):
        for i in self.devices:
            self.devices[i].start()

    def end(self, aPCB):
        self.manageIRQ.endIO(aPCB)