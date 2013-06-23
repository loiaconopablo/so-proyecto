'''
Created on 17/06/2013

@author: Pablo
'''
import abc
from PCB import *
from State import *
import time

class Device:
    __metaclass__ = ABCMeta  # la define como claseAbstracta
    self.listTask = []
    
    def run(self):
        while(True):
            time.sleep(2)
            if self.hayTask():
                tupla = pop(self.task)
                aPCB = tupla[0]
                nextInstruccion=tupla[1]
                aPCB.changeStatus(State.RUNNING)
                nextInstruccion.execute()
                time.sleep(5)   #Simula el tiempo que tarda el dispositivo en ejecutar la 
                aPCB.changeStatus(State.Ready) #instruccion
                

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

    