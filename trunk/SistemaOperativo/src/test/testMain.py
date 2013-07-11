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
Programa1.add(CpuInstruccion1)
Programa1.add(CpuInstruccion2)
Programa1.add(IoInstruccion1)
Programa1.add(IoInstruccion5)
Programa1.add(CpuInstruccion4)
Programa2 = Program("Programa2",2)
Programa2.add(CpuInstruccion4)
Programa2.add(CpuInstruccion5)
Programa2.add(IoInstruccion3)
Programa2.add(IoInstruccion6)
Programa2.add(CpuInstruccion5)
Programa2.add(IoInstruccion4)
Programa2.add(IoInstruccion7)
Programa2.add(CpuInstruccion3)
Programa2.add(IoInstruccion5)
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
Programa3.add(CpuInstruccion1)
Programa3.add(CpuInstruccion2)
Programa3.add(CpuInstruccion2)
Programa4 = Program("Programa4")
Programa4.add(CpuInstruccion1)
Programa4.add(CpuInstruccion2)
Programa4.add(CpuInstruccion3)
Programa4.add(CpuInstruccion4)
Programa4.add(CpuInstruccion5)
Programa4.add(CpuInstruccion1)
Programa4.add(CpuInstruccion2)
Programa5 = Program("Programa5")
Programa5.add(CpuInstruccion1)
Programa5.add(CpuInstruccion2)
Programa5.add(IoInstruccion1)
Programa5.add(IoInstruccion5)
Programa5.add(CpuInstruccion4)



myCDROM = CDROM()
myPrinter = Printer()
myMMU = MMU()
myDiskWithPrograms = Disk()
myDiskWithPrograms.load(Programa1)
myDiskWithPrograms.load(Programa2)
myDiskWithPrograms.load(Programa3)
myDiskWithPrograms.load(Programa4)
myDiskWithPrograms.load(Programa5)
myEmptyDisk = Disk()
asignacionContinua = AsignacionContinua(PrimerAjuste(),myMMU)
myMMU.setLogicalMemory(asignacionContinua)
#myKernel = Kernel(Fifo, myMMU, myEmptyDisk)
myKernel = Kernel(Fifo, myMMU, myDiskWithPrograms)
myKernel.addDevice(myCDROM)
myKernel.addDevice(myPrinter)
myKernel.initializeThread()
myKernel.runProcess("Programa1")
myKernel.runProcess("Programa2")
myKernel.runProcess("Programa3")
myKernel.runProcess("Programa4")
myKernel.runProcess("Programa5")


