import unittest
from find_the_difference import Solution


class FindTheDifferenceTest(unittest.TestCase):
    def test1(self):
        t = Solution().findTheDifference("abcd", "abcde")
        self.assertEqual(t, "e")
    
    def test2(self):
        t = Solution().findTheDifference("","y")
        self.assertEqual(t, "y")

    def test3(self):
        t = Solution().findTheDifference("aa","aaa")
        self.assertEqual(t, "a")
        

if __name__=="__main__":
    unittest.main()