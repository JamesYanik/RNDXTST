from models.warriors import Warrior


class Mage(Warrior):
    def __init__(self):
        super().__init__(60, 30, 10)
