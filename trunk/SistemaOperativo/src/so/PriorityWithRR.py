'''
Created on 23/06/2013

@author: Pablo Loiacono
'''
from RoundRobin.py import *
from Priority.py import *

class PriorityWithRR(Priority, RoundRobin):
    def __init__(self, aQuamtum):
        RoundRobin.__init__(self, aQuamtum)

    def isRR(self):
        RoundRobin.isRR(self)

#===============================================================================
# Se utiliza herencia multiple, solo se utiliza el constructor de RR, y el is RR, el resto
# de los metodos los usa de Priority, ya que se pasa primero como parametro.
#===============================================================================