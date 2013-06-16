'''
Created on 15/06/2013

@author: Pablo
'''
from enum import Enum

class State(Enum):
    READY = "Ready"
    NEW = "New"
    TERMINAED = "Terminated"
    RUNNING = "Running"
    WAITING = "Waiting"