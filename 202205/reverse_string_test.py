import unittest
import reverse_string


class ReverseStringTest(unittest.TestCase):

    def test1(self):
        t = reverse_string.Solution().reverseString(["h","e","l","l","o"])
        self.assertEqual(t, ["o","l","l","e","h"])
    
    def test2(self):
        t = reverse_string.Solution().reverseString(["H","a","n","n","a","h"])
        self.assertEqual(t, ["h","a","n","n","a","H"])

if __name__ == "__main__":
    unittest.main()