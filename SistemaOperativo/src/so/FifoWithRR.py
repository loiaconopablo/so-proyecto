'''
Created on 23/06/2013

@author: Pablo Loiacono
'''
from RoundRobin import *
from Fifo import *

class FifoWithRR(Fifo, RoundRobin):
    def __init__(self, aQuamtum):
        RoundRobin.__init__(self, aQuamtum)

    def isRR(self):
        return True

#===============================================================================
# Se utiliza herencia multiple, solo se utiliza el constructor de RR, el resto
# de los metodos los usa de FIFO, ya que se pasa primero como parametro.
#===============================================================================
