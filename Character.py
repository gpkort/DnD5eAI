
class Character(object):
    MAX_ATTRIBUTE_VALUE = 18
    MIN_ATTRIBUTE_VALUE = 3

    def __init__(self, name: str):
        self.__strength = 0
        self.__intelligence = 0
        self.__wisdom = 0
        self.__dexterity = 0
        self.__charisma = 0
        self.__constitution = 0

        self.validate_name(name)
        self.__name = name

# <editor-fold desc="Attributes properties>

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, val):
        self.validate_attribute(val)
        self.__strength = val

    @property
    def intelligence(self):
        return self.__intelligence

    @intelligence.setter
    def intelligence(self, val):
        self.validate_attribute(val)
        self.__intelligence = val

    @property
    def wisdom(self):
        return self.__wisdom

    @wisdom.setter
    def wisdom(self, val):
        self.validate_attribute(val)
        self.__wisdom = val

    @property
    def dexterity(self):
        return self.__dexterity

    @dexterity.setter
    def dexterity(self, val):
        self.validate_attribute(val)
        self.__dexterity = val

    @property
    def charisma(self):
        return self.__charisma

    @charisma.setter
    def charisma(self, val):
        self.validate_attribute(val)
        self.__charisma = val

    @property
    def constitution(self):
        return self.__constitution

    @constitution.setter
    def constitution(self, val):
        self.validate_attribute(val)
        self.__constitution = val

# </editor-fold>

    @property
    def Name(self) -> str:
        return self.__name

    @Name.setter
    def Name(self, val: str):
        self.validate_name(val)
        self.__name = val

    @staticmethod
    def validate_attribute(val: int):
        if type(val) is not int:
            raise ValueError("Attribute must be an integer")
        if val < Character.MIN_ATTRIBUTE_VALUE:
            raise ValueError("Attribute must be greater than {}".format(Character.MIN_ATTRIBUTE_VALUE))
        if val > Character.MAX_ATTRIBUTE_VALUE:
            raise ValueError("Attribute must be less than {}".format(Character.MAX_ATTRIBUTE_VALUE))

    @staticmethod
    def validate_name(val: str):
        if type(val) is not str:
            raise ValueError("Name must be a string")
        if len(val) == 0:
            raise ValueError("Name cannot be empty")
