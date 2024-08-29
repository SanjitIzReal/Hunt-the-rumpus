"""docstring"""
from character import Enemy
harry = Enemy("CJ", "Blood Crip")
harry.describe()
harry.set_conversation("ahhh shit, here we go again")
harry.talk()
harry.set_weakness("Officer Frank tenpenny")

print("What will you fight with?")
fight_with = input("> ")
harry.fight(fight_with)