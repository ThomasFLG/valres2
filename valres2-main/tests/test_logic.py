import unittest
from app.logic import ajouter, soustraire

class TestLogic(unittest.TestCase):
    def test_ajouter(self):
        self.assertEqual(ajouter(2, 3), 5)
    
    def test_soustraire(self):
        self.assertEqual(soustraire(5, 3), 2)

if __name__ == "__main__":
    unittest.main()
