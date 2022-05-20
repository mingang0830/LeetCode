import unittest
import first_bad_version

class FirstBadVerTest(unittest.TestCase):

    def test1(self):
        t = first_bad_version.Solution().firstBadVersion(5,4)
        self.assertEqual(t,4)
    
    def test2(self):
        t = first_bad_version.Solution().firstBadVersion(1,1)
        self.assertEqual(t,1)
    
    def test3(self):
        t = first_bad_version.Solution().firstBadVersion(2126753390,1702766719)
        self.assertEqual(t,1702766719)


if __name__ == "__main__":
    unittest.main()