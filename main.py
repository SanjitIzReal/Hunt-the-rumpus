from cave import Cave
from character import Enemy

cavern = Cave("Jamaican embassy")
grotto = Cave("Rasta palace")
dungeon = Cave("Skate park")
Street = Cave("Grove Street")
Learningcenter = Cave("Learning Center")
Jail = Cave("Jail")

cavern.set_description("si bomboclatt.")
grotto.set_description("Ya smell dat?.")
dungeon.set_description("Bredda is dat CJ?")
Street.set_description("Dis Da CJ home ya feel")
Learningcenter.set_description("Ay man Leave Da kid Be ah?")
Jail = Cave("bredda why u come here?")

cavern.link_cave("south", grotto)
grotto.link_cave("west", cavern)
cavern.link_cave("east", Street)
Street.link_cave("south", cavern)
Street.link_cave("east",Learningcenter)
Learningcenter.link_cave("north", dungeon)
Jail.link_cave("west", Street)

harry = Enemy("CJ", "Blood Crip")
harry.set_conversation("Wah Gwaan me na see ya in donkey years!")
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
            print("Thats the end of the game")
            current_cave.set_character(None)
        else:
            print("Lata yuh Donkey, Cum Latah")
            dead = True
    else:
        print("There de nuhwan yah tuh fight wid")
    