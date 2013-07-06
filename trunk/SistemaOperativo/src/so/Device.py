'''
Created on 17/06/2013

@author: Pablo
'''
import abc
from State import *
import time
import threading


class Device(threading.Thread):
    def __init__(self, aDeviceManager):
        self.listTask = []
        self.deviceManger= aDeviceManager
        threading.Thread.__init__(self)
    
    def run(self):
        print("Estoy corriendo")#ver depsues
        while(True):
            time.sleep(2)
            if self.hayTask():
                tupla = self.listTask.pop(0)
                aPCB = tupla[0]
                nextInstruccion=tupla[1]
                aPCB.changeStatus(State.RUNNING)
                nextInstruccion.execute()
                time.sleep(5)   #Simula el tiempo que tarda el dispositivo en ejecutar la 
                aPCB.changeStatus(State.Ready) #instruccion
                print("Termine de correr")
                self.deviceManger.end(aPCB)

    def setListTask(self, newvalue):
        self.listTask = newvalue
    
    def getListTaks(self, newvalue):
        return self.listTask

    @abc.abstractclassmethod
    def addTask(self, aPCB, nextInstruccion):
        tupla = (aPCB,nextInstruccion)
        self.value_getter().append(tupla)
        
    def hayTask(self):
        return len(self.value_getter())>0

class Printer(Device):
    pass

    