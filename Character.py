
class Character(object):

    def __init__(self, strength: int):
        self.__strength = strength


    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, val):
        pass

