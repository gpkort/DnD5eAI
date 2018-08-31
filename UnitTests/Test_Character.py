import unittest
from Character import Character


class TestsCharacter(unittest.TestCase):
    def setUp(self):
        self.testChar = Character(name="Greg")

    def test__init(self):
        self.assertEqual(self.testChar.strength, 0, "strength ctor test failed")
        self.assertEqual(self.testChar.intelligence, 0, "intelligence ctor test failed")
        self.assertEqual(self.testChar.wisdom, 0, "wisdom ctor test failed")
        self.assertEqual(self.testChar.dexterity, 0, "dexterity ctor test failed")
        self.assertEqual(self.testChar.charisma, 0, "charisma ctor test failed")
        self.assertEqual(self.testChar.constitution, 0, "constitution ctor test failed")
        self.assertEqual(self.testChar.XP, 0, "experience points ctor test failed")

        self.assertEqual(self.testChar.Name, "Greg", "name ctor test failed")

# <editor-fold desc="Attributes tests">

    def test_strengthTooLow(self):
        self.assertRaises(ValueError, setattr, self.testChar, "strength", 0)

    def test_strengthTooHigh(self):
        self.assertRaises(ValueError, setattr, self.testChar, "strength", 20)

    def test_strengthNotInt(self):
        self.assertRaises(ValueError, setattr, self.testChar, "strength", 0.5)

    # Intelligence Tests

    def test_intelligenceTooLow(self):
        self.assertRaises(ValueError, setattr, self.testChar, "intelligence", 0)

    def test_intelligenceTooHigh(self):
        self.assertRaises(ValueError, setattr, self.testChar, "intelligence", 20)

    def test_intelligenceNotInt(self):
        self.assertRaises(ValueError, setattr, self.testChar, "intelligence", 0.5)

    # Wisdom Tests

    def test_wisdomTooLow(self):
        self.assertRaises(ValueError, setattr, self.testChar, "wisdom", 0)

    def test_wisdomTooHigh(self):
        self.assertRaises(ValueError, setattr, self.testChar, "wisdom", 20)

    def test_wisdomNotInt(self):
        self.assertRaises(ValueError, setattr, self.testChar, "wisdom", 0.5)

    # dexterity Tests

    def test_dexterityTooLow(self):
        self.assertRaises(ValueError, setattr, self.testChar, "dexterity", 0)

    def test_dexterityTooHigh(self):
        self.assertRaises(ValueError, setattr, self.testChar, "dexterity", 20)

    def test_dexterityNotInt(self):
        self.assertRaises(ValueError, setattr, self.testChar, "dexterity", 0.5)

    # charisma Tests

    def test_charismaTooLow(self):
        self.assertRaises(ValueError, setattr, self.testChar, "charisma", 0)

    def test_charismaTooHigh(self):
        self.assertRaises(ValueError, setattr, self.testChar, "charisma", 20)

    def test_charismaNotInt(self):
        self.assertRaises(ValueError, setattr, self.testChar, "charisma", 0.5)

    # charisma Tests

    def test_constitutionTooLow(self):
        self.assertRaises(ValueError, setattr, self.testChar, "constitution", 0)

    def test_constitutionTooHigh(self):
        self.assertRaises(ValueError, setattr, self.testChar, "constitution", 20)

    def test_constitutionNotInt(self):
        self.assertRaises(ValueError, setattr, self.testChar, "constitution", 0.5)
# </editor-fold>

    def test_nameNotStr(self):
        self.assertRaises(ValueError, setattr, self.testChar, "Name", 20)

    def test_nameEmpty(self):
        self.assertRaises(ValueError, setattr, self.testChar, "Name", "")

    def test_xpNotInt(self):
        self.assertRaises(ValueError, setattr, self.testChar, "XP", 2.5)
        self.assertRaises(ValueError, setattr, self.testChar, "XP", "20")

    def test_xpNegaitve(self):
        self.assertRaises(ValueError, setattr, self.testChar, "XP", -1)



# if __name__ == '__main__':
#     unittest.main()


# @unittest.expectedFailure
