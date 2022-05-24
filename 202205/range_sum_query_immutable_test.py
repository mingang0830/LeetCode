import unittest
import range_sum_query_immutable


class RangeSumQueryImmutableTest(unittest.TestCase):
    init_ = range_sum_query_immutable.NumArray([-2, 0, 3, -5, 2, -1])

    def test1(self):    
        t = self.init_.sumRange(0,2)
        self.assertAlmostEqual(t, 1)
    
    def test2(self):    
        t = self.init_.sumRange(2,5)
        self.assertAlmostEqual(t, -1)
    
    def test3(self):    
        t = self.init_.sumRange(0,5)
        self.assertAlmostEqual(t, -3)

if __name__=="__main__":
    unittest.main()