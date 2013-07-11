'''
Created on 10/07/2013

@author: Pablo Loiacono
'''
import unittest
from FifoWithRR import *
from PCB import *


class TestWithRR(unittest.TestCase):


    def setUp(self):
        self.policity = FifoWithRR(8)
        self.aPCB = PCB("Program1")
        self.bPCB = PCB("Program2", 20)
        self.cPCB = PCB("Program2", 50)
        self.dPCB = PCB("Program2", 15)

    def tearDown(self):
        pass
    
    def testBuilder(self):
        self.assertEquals(len(self.policity.qReady),0)
        self.assertEquals(self.policity.getQuantum(),8)
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
        self.assertEquals(self.policity.next(), self.aPCB)
        self.assertEquals(self.policity.next(), self.bPCB)

    def testRetryAdd(self):
        self.policity.retryAdd(self.aPCB)
        self.policity.retryAdd(self.bPCB)
        self.assertEquals(self.policity.qReady[0].priority, 10)
        self.assertEquals(self.policity.qReady[1].priority, 20)
 
suite = unittest.TestLoader().loadTestsFromTestCase(TestWithRR)
unittest.TextTestRunner(verbosity=2).run(suite)
