import unittest
from members import checkInput
from providers import findProvider

class memberTesting(unittest.TestCase):
    def test_checkInput(self):
        result = checkInput("Jack", "9714701489", "1122 HOHO", "Portland", "OR", "97034")
        self.assertEqual(result, True)

    def test_checkInput_name_ValueError(self):
        with self.assertRaises(ValueError):
            checkInput("1234", "9714701489", "1122 HOHO", "Portland", "OR", "97034")

    def test_checkInput_phone_ValueError(self):
        with self.assertRaises(ValueError):
            checkInput("jack", "971kijik", "1122 HOHO", "Portland", "OR", "97034")
    
    def test_checkInput_state_ValueError_1(self):
        with self.assertRaises(ValueError):
            checkInput("jack", "9714701489", "1122 HOHO", "Portland", "ORG", "97034")

    def test_checkInput_state_ValueError_2(self):
        with self.assertRaises(ValueError):
            checkInput("jack", "9714701489", "1122 HOHO", "Portland", "11", "97034")

    def test_checkInput_zip_ValueError_1(self):
        with self.assertRaises(ValueError):
            checkInput("jack", "9714701489", "1122 HOHO", "Portland", "11", "lolo")

    def test_checkInput_zip_ValueError_2(self):
        with self.assertRaises(ValueError):
            checkInput("jack", "9714701489", "1122 HOHO", "Portland", "11", "9070342")

class providerTesting(unittest.TestCase):
    def test_findProvider(self):
        result = findProvider("123456789")
        self.assertTrue(type(result) is str)



if __name__ == "__main__":
    unittest.main()
