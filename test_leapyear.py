import unittest
import leapyear

class TestCase(unittest.TestCase):
    def test_leapyear1(self):
        result = leapyear.leapyear(2000)
        self.assertEqual(1, result)
    def test_leapyear2(self):
        result = leapyear.leapyear(100)
        self.assertEqual(0, result)
    def test_leapyear3(self):
        result = leapyear.leapyear("200")
        self.assertEqual(0, result)
    def test_leapyear4(self):
        result = leapyear.leapyear("number")
        self.assertEqual(0, result)
    def test_leapyear5(self):
        result = leapyear.leapyear(None)
        self.assertEqual(0, result)


if __name__ == '__main__':

    unittest.main()
    