import unittest
from animal import Animal

class TestAnimal(unittest.TestCase):
    
    def testgetNom(self):
        animal = Animal("Chat", "chaiuit", 0.3, 8, 14)
        self.assertEqual("Chat", animal.getNom(), "Err: le nom est mauvais")

    def testcomparaisonOK(self):
        chat = Animal("Chat", "chaiuit", 0.3, 8, 14)
        lion = Animal("Lion", "lionde", 1.2, 120, 14)
        self.assertEqual(True, chat.comparer(lion), "Err: l'animal comparée est plus petit que l'autre animal")

    def testcomparaisonNOT(self):
        chat = Animal("Chat", "chaiuit", 0.3, 8, 14)
        lion = Animal("Lion", "lionde", 1.2, 120, 14)
        self.assertEqual(False, lion.comparer(chat), "Err: l'animal comparée est plus grand que l'autre animal")

if __name__ == '__main__':
    unittest.main()