from cave import Cave
from character import Enemy


cavern = Cave("Cavern")
grotto = Cave("Grotto")
dungeon = Cave("Dungeon")

cavern.set_description("A damp and dirty cave.")
grotto.set_description("A small cave with ancient markings.")
dungeon.set_description("A large cave with a rack.")

cavern.link_cave("south", dungeon)
dungeon.link_cave("north", cavern)
dungeon.link_cave("west", grotto)
grotto.link_cave("east", dungeon)

harry = Enemy("CJ", "A smelly Wumpus")
harry.set_conversation("ahhh shit, here we go again")
harry.set_weakness("Officer Frank tenpenny")
dungeon.set_character(harry)

current_cave = cavern
while True:
    print("\n")
    current_cave.get_details()
    inhabitant = current_cave.character
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")
    current_cave = current_cave.move(command)
    