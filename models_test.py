import unittest
from io import StringIO
from datetime import datetime
from unittest.mock import patch
from members import checkInput, Members, createMember, findMember
from providers import findProvider, createProvider, Provider
from services import Service, getreport

class memberFunctions(unittest.TestCase):
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

    def test_createMember(self):
        mem = ["Jack", "123456789", "1234 Holo", "Portland", "OR", "97201"]
        with patch('builtins.input', side_effect=mem):
            temp = createMember()
        self.assertEqual(len(temp), 6)

    def test_createMember_toLower(self):
        mem = ["Jack", "123456789", "1234 Holo", "Portland", "OR", "97201"]
        exceptOp = ["jack", "123456789", "1234 holo", "portland", "or", "97201"]
        with patch('builtins.input', side_effect=mem):
            temp = createMember()
        self.assertEqual(temp, exceptOp)

    def test_member_class(self):
        mem = Members("Test1", "5031112222", "1234 Holo", "Portland", "OR", "97201")
        self.assertTrue(type(mem) is Members)

    def test_findMember(self):
        result = findMember("1112223333")
        self.assertTrue(type(result) is str)



class providerTesting(unittest.TestCase):

    def test_findProvider(self):
        result = findProvider("2223334444")
        self.assertTrue(type(result) is str)

    def test_createProvider(self):
        pro = ["Test", "5031112222", "Internal"]
        with patch('builtins.input', side_effect=pro):
            temp = createProvider()
        self.assertEqual(len(temp), 3)

    def test_createProvider_toLower(self):
        pro = ["Test", "5031112222", "Internal"]
        expectOp = ["test", "5031112222", "internal"]
        with patch('builtins.input', side_effect=pro):
            temp = createProvider()
        self.assertEqual(temp, expectOp)

    def test_provider_class(self):
        temp = Provider("testone", "5032223333", "brain")
        self.assertTrue(type(temp) is Provider)


class serviceTesting(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_getReport(self, mock_stdout):
        getreport("00", "00")
        self.assertEqual(mock_stdout.getvalue(), "This is for unittest\n\n")
    
    def test_service_class(self):
        sv = ["9", "9", "2099", "123456", "2223334444", "1112223333", "unittest's note", "1000"]
        with patch('builtins.input', side_effect = sv): 
            temp = Service()
        self.assertTrue(type(temp) is Service)
    
    def test_service_getTime(self):
        sv = ["9", "9", "2099", "123456", "123456789", "9714701489", "unittest's note", "1000"]
        with patch('builtins.input', side_effect = sv): 
            temp = Service()
            time = temp.getTime()
        self.assertEqual(time, datetime.now().strftime("%m-%d-%Y %H:%M"))

    def test_service_getMonthWeek(self):
        sv = ["9", "9", "2099", "123456", "123456789", "9714701489", "unittest's note", "1000"]
        with patch('builtins.input', side_effect = sv): 
            temp = Service()
            time = temp.getMonthWeek()
        self.assertEqual(time, datetime.now().strftime("%m-%W"))





if __name__ == "__main__":
    unittest.main()
