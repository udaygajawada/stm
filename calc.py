"""first demo program"""

def add(x,y):
    return x+y

import unittest

class Add_TestCase(unittest.TestCase):
    def test1(self):
        for i in range(0,10):
            for j in range(0,10):
                assert add(i/2,j/2) == (i + j)/2        

if __name__ == "__main__":
    unittest.main(verbosity=1)
