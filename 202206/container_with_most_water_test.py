import unittest
from container_with_most_water import Solution


class FindTheDifferenceTest(unittest.TestCase):
    def test1(self):
        t = Solution().maxArea([1,8,6,2,5,4,8,3,7])
        self.assertEqual(t, 49)
    
    def test2(self):
        t = Solution().maxArea([1,1])
        self.assertEqual(t, 1)

    def test3(self):
        t = Solution().maxArea([1,2,1])
        self.assertEqual(t, 2)
        

if __name__=="__main__":
    unittest.main()