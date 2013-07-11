'''
Created on 10/07/2013

@author: Pablo Loiacono
'''
import unittest
from IOInstruccion import *


class TestIOInstruccion(unittest.TestCase):


    def setUp(self):
        self.first = IOInstruccion("Imprimir Pagina. ", "Printer")

    def tearDown(self):
        pass
    
    def testBuilder(self):
        self.assertEquals(type(self.first.deviceName), str)
        self.assertEquals(type(self.first.action), str)
        
    def testIsIO(self):
        self.assertTrue(self.first.isIO())
    
    def testGetDeviceName(self):
        self.assertEquals(self.first.getDeviceName(), "Printer")
        