import unittest
import parsers

class Test_main(unittest.TestCase):

    def test_scientific(self):
        assert parsers.parse("1.4E-5") == "14*10**-6"
        assert parsers.parse("+0045") == None
        assert parsers.parse("8.34e+3") == "834*10**1"
        assert parsers.parse("25.e25") == None
        #assert parsers.parse(".5e-2") == "5*10**-3"


if __name__ == '__main__':
    unittest.main(verbosity=2)
