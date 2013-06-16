'''
Created on 10/06/2013

@author: Pablo
'''

class HandlerIO:  # preguntar si tiene que ser otro Thread mas
    def __init__(self, aDeviceMange):
        self.deviceManage = aDeviceManage
        self.task = []
        
    def getDevice(self, IOInstruction):
        deviceIOInstruction = IOInstruction.getDevice()
        return self.deviceManage.get(deviceIOInstruction)
    
    def handleIO(self, aPCB):
        aPCB.changeStatus(State.WAITING)
        self.task.append(aPCB)
        
    def run(self):
        while(True):
            sleep(1)
            if self.hayTask():
                aPCB = pop(self.task)
                instruccion = self.getNextInstruction(aPCB.nextDirInstruccion())
                self.getDevice(instruccion).run()##### hay que seguirlo
            
            
    def getNextInstruction(self, nextDir):
        self.deviceManage.get(Device.DISK)  # Crear un Enum para los dispositivos o ver como hacer
        instruccion = self.memory.read(aDirForInstruccion)
        return instruction
    
    def hayTask(self):
        return len(self.task)
            
    
