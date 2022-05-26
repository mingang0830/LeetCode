import unittest
from counting_bits import Solution


class CountingBitsTest(unittest.TestCase):
    def test1(self):
        t = Solution().countBits(2)
        self.assertEqual(t,[0,1,1])
    
    def test2(self):
        t = Solution().countBits(5)
        self.assertEqual(t,[0,1,1,2,1,2])

if __name__=="__main__":
    unittest.main()