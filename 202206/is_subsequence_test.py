import unittest
from is_subsequence import Solution


class IsSubsequenceTest(unittest.TestCase):
    def test1(self):
        t = Solution().isSubsequence("abc","ahbgdc")
        self.assertEqual(t, True)
    
    def test2(self):
        t = Solution().isSubsequence("axc","ahbgdc")
        self.assertEqual(t, False)

    def test3(self):
        t = Solution().isSubsequence("ace","abcde")
        self.assertEqual(t, True)
        

if __name__=="__main__":
    unittest.main()