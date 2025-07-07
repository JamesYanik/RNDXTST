from models.warriors import Character


def check_hp(character: Character):
    if character.hp <= 0:
        character.hp = 0
        print("DEAD!!!")
