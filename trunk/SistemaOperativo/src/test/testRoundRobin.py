'''
Created on 10/07/2013

@author: Pablo Loiacono
'''
import unittest
from RoundRobin import *
from PCB import *


class TestRoundRobin(unittest.TestCase):


    def setUp(self):
        self.policity = RoundRobin(5)
        self.aPCB = PCB("Program1")
        self.bPCB = PCB("Program2", 20)
        self.cPCB = PCB("Program2", 50)
        self.dPCB = PCB("Program2", 15)

    def tearDown(self):
        pass
    
    def testBuilder(self):
        self.assertEquals(len(self.policity.qReady),0)
        self.assertEquals(self.policity.getQuantum(),5)
        self.assertTrue(self.policity.isRR())
        
    def testAdd(self):
        self.policity.add(self.aPCB)
        self.policity.add(self.bPCB)
        self.policity.add(self.cPCB)
        self.policity.add(self.dPCB)
        self.assertEquals(self.policity.qReady[0], self.aPCB)
        self.assertEquals(self.policity.qReady[1], self.bPCB)
        self.assertEquals(self.policity.qReady[2], self.cPCB)
        self.assertEquals(self.policity.qReady[3], self.dPCB)

suite = unittest.TestLoader().loadTestsFromTestCase(TestRoundRobin)
unittest.TextTestRunner(verbosity=2).run(suite)