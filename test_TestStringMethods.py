import unittest
import add_1

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        result= add_1.add_1(2,4)
        self.assertEqual(result, 6)

    def test_upper_sub(self):
        result= add_1.sub_1(6,4)
##        self.assertEqual(result, 2)
        self.assertFalse(result)


    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())






##    def test_split(self):
##        s = 'hello world'
##        self.assertEqual(s.split(), ['hello', 'world'])
##        # check that s.split fails when the separator is not a string
##        with self.assertRaises(TypeError):
##            s.split(2)

if __name__ == '__main__':
    unittest.main()
