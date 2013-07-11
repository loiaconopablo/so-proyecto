'''
Created on 10/07/2013

@author: Pablo Loiacono
'''
import unittest
from PriorityWithRR import *
from PCB import *
from RoundRobin import *


class TestPrioriryWhitRR(unittest.TestCase):


    def setUp(self):
        self.policity = PriorityWithRR(18)
        self.aPCB = PCB("Program1")
        self.bPCB = PCB("Program2", 20)
        self.cPCB = PCB("Program2", 50)
        self.dPCB = PCB("Program2", 15)
        self.ePCB = PCB("Program2", 5)

    def tearDown(self):
        pass
    
    def testBuilder(self):
        self.assertEquals(len(self.policity.qReady),0)
        self.assertEquals(self.policity.getQuantum(),18)
        self.assertTrue(self.policity.isRR())
        
    def testAddYNext(self):
        self.policity.add(self.aPCB)
        self.policity.add(self.bPCB)
        self.policity.add(self.cPCB)
        self.policity.add(self.dPCB)
        self.policity.add(self.ePCB)
        self.assertEquals(self.policity.qReady[0], self.ePCB)
        self.assertEquals(self.policity.qReady[1], self.aPCB)
        self.assertEquals(self.policity.qReady[2], self.dPCB)
        self.assertEquals(self.policity.qReady[3], self.bPCB)
        self.assertEquals(self.policity.qReady[4], self.cPCB)
        self.assertEquals(self.policity.next(), self.ePCB)
        self.assertEquals(self.policity.next(), self.aPCB)
 
    def testRetryAdd(self):
        self.policity.retryAdd(self.aPCB)
        self.policity.retryAdd(self.bPCB)
        self.assertEquals(self.policity.qReady[0].priority, 9)
        self.assertEquals(self.policity.qReady[1].priority, 19)
 

suite = unittest.TestLoader().loadTestsFromTestCase(TestPrioriryWhitRR)
unittest.TextTestRunner(verbosity=2).run(suite)