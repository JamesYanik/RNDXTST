class Character:
    def __init__(self, hp, atk, spd):
        self.hp = hp
        self.atk = atk
        self.spd = spd


class Fighter(Character):
    def __init__(self):
        super().__init__(100, 10, 20)

