"""first demo program"""

def test(x):
    return x

import unittest

class Add_TestCase(unittest.TestCase):
    def test1(self):
        assert test(11.123) == 11.123 
	
if __name__ == "__main__":
    unittest.main(verbosity=2)
