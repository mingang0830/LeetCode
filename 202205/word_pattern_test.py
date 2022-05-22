import unittest
import word_pattern

class WordPatternTest(unittest.TestCase):
    def test1(self):
        t = word_pattern.Solution().wordPattern("abba", "dog cat cat dog")
        self.assertAlmostEqual(t, True)
    
    def test2(self):
        t = word_pattern.Solution().wordPattern("abba", "dog cat cat fish")
        self.assertAlmostEqual(t, False)
    
    def test3(self):
        t = word_pattern.Solution().wordPattern("aaaa", "dog cat cat dog")
        self.assertAlmostEqual(t, False)
    
    def test4(self):
        t = word_pattern.Solution().wordPattern("aba", "dog cat cat")
        self.assertAlmostEqual(t, False)
if __name__=="__main__":
    unittest.main()