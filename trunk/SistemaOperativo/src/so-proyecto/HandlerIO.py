'''
Created on 10/06/2013

@author: Pablo
'''

class HandlerIO:
    def __init__(self, aDeviceMange):
        self.deviceManage = aDeviceManage
        self.devices = {}
        self.devices[Printer()] = Printer.thread # ver bien
        
    def getDevice(self, IOInstruction):
        deviceInstrdeviceIOInstruction = IOInstruction.getDevice()
        return self.deviceManage.get(deviceIOInstruction)