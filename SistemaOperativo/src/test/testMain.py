'''
Created on 04/07/2013

@author: Pablo Loiacono
'''

from Kernel import *
from AsignacionContinua import *
from MemPolicity import *
from Fifo import *
from RoundRobin import *
from Priority import *
from Device import *
from IOInstruccion import *
from Instruccion import *
from Program import *
from Disk import *


#FACTORY
IoInstruccion1 = IOInstruccion("Imprimir Pagina 1. ", "Printer")
IoInstruccion2 = IOInstruccion("Imprimir Pagina 2. ", "Printer")
IoInstruccion3 = IOInstruccion("Imprimir Pagina 3. ", "Printer")
IoInstruccion4 = IOInstruccion("Imprimir Pagina 4. ", "Printer")
IoInstruccion5 = IOInstruccion("Imprimir Pagina 5. ", "Printer")
IoInstruccion6 = IOInstruccion("Leer Pista 1. ", "CDROM")
IoInstruccion7 = IOInstruccion("Leer Pista 2. ", "CDROM")
IoInstruccion8 = IOInstruccion("Leer Pista 3. ", "CDROM")
IoInstruccion9 = IOInstruccion("Leer Pista 4. ", "CDROM")
IoInstruccion10 = IOInstruccion("Leer Pista 5. ", "CDROM")
CpuInstruccion1= Instruccion("Instruccion de CPU #1")
CpuInstruccion2= Instruccion("Instruccion de CPU #2")
CpuInstruccion3= Instruccion("Instruccion de CPU #3")
CpuInstruccion4= Instruccion("Instruccion de CPU #4")
CpuInstruccion5= Instruccion("Instruccion de CPU #5")

Programa1 = Program("Programa1")
Programa1.add(CpuInstruccion5)
Programa1.add(CpuInstruccion3)
Programa1.add(IoInstruccion2)
Programa1.add(IoInstruccion10)
Programa1.add(IoInstruccion9)
Programa1.add(CpuInstruccion3)
Programa1.add(IoInstruccion7)
Programa2 = Program("Programa2",2)
Programa2.add(IoInstruccion4)
Programa2.add(IoInstruccion1)
Programa2.add(CpuInstruccion2)
Programa2.add(CpuInstruccion4)
Programa2.add(CpuInstruccion1)
Programa2.add(IoInstruccion10)
Programa2.add(IoInstruccion6)
Programa2.add(CpuInstruccion5)
Programa2.add(IoInstruccion1)
Programa3 = Program("Programa3",15)
Programa3.add(CpuInstruccion1)
Programa3.add(CpuInstruccion2)
Programa3.add(CpuInstruccion3)
Programa3.add(CpuInstruccion4)
Programa3.add(CpuInstruccion5)
Programa3.add(CpuInstruccion1)
Programa3.add(CpuInstruccion2)
Programa3.add(CpuInstruccion3)
Programa3.add(CpuInstruccion4)
Programa3.add(CpuInstruccion5)


myCDROM = CDROM()
myPrinter = Printer()
myMMU = MMU()
myDiskWithPrograms = Disk()
myDiskWithPrograms.load(Programa1)
myDiskWithPrograms.load(Programa2)
myEmptyDisk = Disk()
asignacionContinua = AsignacionContinua(PrimerAjuste(),myMMU)
myMMU.setLogicalMemory(asignacionContinua)
myKernel = Kernel(Fifo(), myMMU, myDiskWithPrograms)
myKernel.addDevice(myCDROM)
myKernel.addDevice(myPrinter)
myKernel.initializeThread()
myKernel.runProcess("Programa1")



