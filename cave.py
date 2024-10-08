class Cave:
    def __init__(self, cave_name):
        self.name = cave_name
        self.description = None
        self.linked_caves = {}
        self.character = None

    def set_name(self,cave_name):
        self.name = cave_name

    def get_name(self):
        return self.name

    def set_description(self, cave_description):
        self.description = cave_description

    def get_description(self):
        return self.description

    def describe(self):
        print(self.description)

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character

    def link_cave(self, direction, cave_to_link):
        self.linked_caves[direction] = cave_to_link
        #print(self.name + " linked caves: " + repr(self.linked_caves))

    def get_details(self):
        print(self.name)
        print("----------")
        print(self.description)
        for direction, cave in self.linked_caves.items():
            print("The " + cave.get_name() + " is " + direction)

    def move(self, direction):
        """Manages movement between caves"""
        if direction in self.linked_caves:
            return self.linked_caves[direction]
        else:
            print("You cannot go that way")
            return self
        