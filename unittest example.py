import unittest
class TestStringMethods(unittest.Testcase):
    def setup(self):
        pass
    #Returns True if the string contains 4 a.
    def test_strings_a(self):
        self.assertEqual('a'*4,'aa')
        assertEqual

    def test_string_concat(self):
        self.assertEqual("a"+"b","ab")

        #Returns True if the string is in upper case.
    def test_upper(self):
        self.assertEqual('PYTHON'.upper(),'PYTHON')
        #returns if the