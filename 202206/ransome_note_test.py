import unittest
from ransome_note import Solution


class GuessNumberTest(unittest.TestCase):
    def test1(self):
        t = Solution().canConstruct("a", "b")
        self.assertEqual(t, False)
    
    def test2(self):
        t = Solution().canConstruct("aa", "ab")
        self.assertEqual(t, False)

    def test3(self):
        t = Solution().canConstruct("aa", "aab")
        self.assertEqual(t, True)
    
    def test4(self):
        t = Solution().canConstruct("fihjjjjei", "hjibagacbhadfaefdjaeaebgi")
        self.assertEqual(t, False)
    

if __name__=="__main__":
    unittest.main()