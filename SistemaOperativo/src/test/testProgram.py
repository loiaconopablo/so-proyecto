'''
Created on 10/07/2013

@author: Pablo Loiacono
'''
import unittest
from Program import *
from Instruccion import *
from IOInstruccion import *


class TestProgram(unittest.TestCase):


    def setUp(self):
        self.programa = Program("FirstProgram",5)
        self.programaB = Program("SecondProgram")
        self.instruccionA = Instruccion("Accion 1")
        self.instruccionB = Instruccion("Accion 2")
        self.instruccionC = Instruccion("Accion 3")
        self.instruccionD = IOInstruccion("Imprimir Pagina. ", "Printer")
        self.instruccionE = IOInstruccion("Leer CD. ", "CDROM")

    def tearDown(self):
        pass
    
    def testBuilder(self):
        self.assertEquals(len(self.programa.instruction),0)
        self.assertFalse(self.programa.isInMemory())
        self.assertEquals(self.programa.priority,5)
        self.assertEquals(self.programaB.priority,10)
        
    def testAddyGetSize(self):
        self.programa.add(self.instruccionA)
        self.programa.add(self.instruccionB)
        self.assertEquals(len(self.programa.instruction),2)
        self.assertEquals(self.programa.getSize(),2)
        self.programa.add(self.instruccionC)
        self.programa.add(self.instruccionD)
        self.programa.add(self.instruccionE)
        self.assertEquals(self.programa.getSize(),5)
        
    def testgetName(self):
        self.assertEquals(self.programa.getName(),"FirstProgram")

    def testLoadInMemory(self):
        self.programa.loadInMemory()
        self.assertTrue(self.programa.isInMemory())
        
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestProgram)
unittest.TextTestRunner(verbosity=2).run(suite)