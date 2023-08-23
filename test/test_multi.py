import unittest
from app.multi import multiplicar

class TestMultiplicar(unittest.TestCase):

    
    def test_multiplicacion_positiva(self):
        self.assertEqual(multiplicar(2, 3), 6) 

    
    def test_multiplicacion_negativa(self):
        self.assertEqual(multiplicar(-2, 3), -6)  

if __name__ == '__main__':
    unittest.main()