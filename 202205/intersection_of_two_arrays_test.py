import unittest
from intersection_of_two_arrays import Solution


class IntersectionTest(unittest.TestCase):
    def intersection1_test1(self):
        t = Solution().intersection([1,2,2,1],[2,2])
        self.assertAlmostEqual(t,[2])
    
    def intersection1_test2(self):
        t = Solution().intersection([4,9,5],[9,4,9,8,4])
        self.assertAlmostEqual(t,[4,9])
    
    def intersection2_test1(self):
        t = Solution().intersection2([1,2,2,1],[2,2])
        self.assertAlmostEqual(t,[2,2])
    
    def intersection2_test2(self):
        t = Solution().intersection2([4,9,5],[9,4,9,8,4])
        self.assertAlmostEqual(t,[9,4])
    

if __name__ == "__main__":
    unittest.main()