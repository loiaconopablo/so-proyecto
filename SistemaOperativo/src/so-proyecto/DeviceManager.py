'''
Created on 15/06/2013

@author: Pablo
'''
from PCB import *
from Device import *

class DeviceManager:
    def __init__(self):
        self.devices = {}
        self.devices[Printer()] = Printer.thread  # ver bien       
        
    def get(self, aNameDevice):
        return self.devices[aNameDevice]
    
    def handle(self, aDevice , aPCB, nextInstruccion):
        device = self.get(aDevice)
        device.addTask(aPCB, nextInstruccion)
        
