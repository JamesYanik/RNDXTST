from models.warriors import Character


def move_up(character: Character):
    print(character, "moving up")


def move_down(character: Character):
    print(character, "moving down")


def move_left(character: Character):
    print(character, "moving left")


def move_right(character: Character):
    print(character, "moving right")


def deal_damage(character: Character, damage: int):
    character.hp -= damage
    print(f"{character} dealt {damage} damage")
