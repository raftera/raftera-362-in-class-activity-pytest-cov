import unittest
import leapyear

class TestCase(unittest.TestCase):
    def test_leapyear1(self):
        result = leapyear.leapyear(2000)
        self.assertEqual(1, result)



if __name__ == '__main__':

    unittest.main()
    