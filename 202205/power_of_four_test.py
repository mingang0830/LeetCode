import unittest
from power_of_four import Solution


class PowerOfFourTest(unittest.TestCase):
    def test1(self):
        t = Solution().isPowerOfFour(16)
        self.assertEqual(t, True)

    def test2(self):
        t = Solution().isPowerOfFour(5)
        self.assertEqual(t, False)

    def test3(self):
        t = Solution().isPowerOfFour(1)
        self.assertEqual(t, True)
    
    def test4(self):
        t = Solution().isPowerOfFour(0)
        self.assertEqual(t, False)

if __name__ == "__main__":
    unittest.main()