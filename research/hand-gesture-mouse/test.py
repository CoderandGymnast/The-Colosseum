import unittest
import statistics
import math
import numpy as np 
from numpy import linalg as la

class TestAPIs(unittest.TestCase):

    def testcase_0(self):
        self.assertAlmostEqual(statistics.stdev(
            [1,2,3,4,5]), math.sqrt(10/4)) 

    def testcase_1(self):
        self.assertAlmostEqual(np.std(
            [1,2,3,4,5]), math.sqrt(10/5)) 
        
    def testcase_2(self):
        self.assertAlmostEqual(la.norm(np.subtract([0,0],[1,1])),math.sqrt(2))
        
    def testcase_3(self):
        self.assertAlmostEqual(la.norm(np.subtract([1,2],[4,2.5])),math.sqrt(9.25))
    

if __name__ == '__main__':
    unittest.main()
