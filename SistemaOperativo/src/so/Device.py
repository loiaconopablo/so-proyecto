'''
Created on 17/06/2013

@author: Pablo
'''
import abc
from State import *
import time
import threading


class Device(threading.Thread):
    def __init__(self):
        if type(self) is Device:
            raise NotImplementedError('Can\'t instantiate class ' + self.__class__.__name__ )
        else:
            self.listTask = []
            self.deviceManger = None
            threading.Thread.__init__(self)
    
    def run(self):
        print("Starting a " + self.__class__.__name__)
        while(True):
            time.sleep(2)
            if self.hayTask():
                tupla = self.listTask.pop(0)
                aPCB = tupla[0]
                nextInstruccion = tupla[1]
                aPCB.changeStatus(State.RUNNING)
                time.sleep(2)  # Simula el tiempo que tarda el dispositivo en ejecutar la 
                nextInstruccion.execute()
                aPCB.changeStatus(State.READY)  # instruccion
                print(self.__class__.__name__+" ending instruction execution of IO.")
                self.deviceManger.end(aPCB)

    def setManager(self, aDeviceManager):
        self.deviceManger = aDeviceManager
        
    def setListTask(self, newvalue):
        self.listTask = newvalue
    
    def getListTaks(self):
        return self.listTask

    def addTask(self, aPCB, nextInstruccion):
        tupla = (aPCB, nextInstruccion)
        self.getListTaks().append(tupla)
        
    def hayTask(self):
        return len(self.getListTaks()) > 0
    
    def getName(self):
        return self.__class__.__name__

class Printer(Device):
    pass

class CDROM(Device):
    pass
    
