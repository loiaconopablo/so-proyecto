'''
Created on 17/06/2013

@author: Pablo
'''
import abc
from PCB import *
from State import *

class Device:
    __metaclass__ = ABCMeta  # la define como claseAbstracta
    
    @abc.abstractclassmethod
    def run(self):
        while(True):
            sleep(1)
            if self.hayTask():
                aPCB = pop(self.task)
                instruccion = aPCB.nextDirInstruccion()#CONTINUAR
                aPCB.changeStatus(State.RUNNING)
               
                print()

    def value_getter(self):
        return 'Should never see this'
    
    def value_setter(self, newvalue):
        return

    listTask = abc.abstractproperty(value_getter, value_setter)

    @abc.abstractclassmethod
    def addTask(self):
        self 
    def hayTask(self):
        return len(self.value_getter())>0

class Printer(Device):
    _listTask = []
    
    def value_getter(self):
        return self._listTask

    def value_setter(self, newvalue):
        self._listTask = newvalue
    
    def addTask(self, aTask):
        self._listTask.append(aTask)

    value = property(value_getter, value_setter)
    