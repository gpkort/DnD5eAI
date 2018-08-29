import unittest
from Character import Character



class TestsCharacter(unittest.TestCase):

    def test_strength_init(self):
        character = Character(3)
        self.assertEqual(character.strength, 3)