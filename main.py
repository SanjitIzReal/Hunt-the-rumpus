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

harry = Enemy("CJ", "Blood Crip")
harry.set_conversation("Come closer. I can't see you!")
harry.set_weakness("vegemite")
dungeon.set_character(harry)

current_cave = cavern
dead = False
while dead is False:
    print("\n")
    current_cave.get_details()
    inhabitant = current_cave.character
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")
    if command in ["north", "south", "east", "west"]:
        current_cave = current_cave.move(command)
    elif command == "talk":
        if inhabitant is not None: 
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("Bomboclatt Bredrin yu win di fight")
            current_cave.set_character(None)
        else:
            print("Lata yuh Donkey, Cum Latah")
            print("Thats the end of the game")
            dead = True
    else:
        print("There de nuhwan yah tuh fight wid")
    