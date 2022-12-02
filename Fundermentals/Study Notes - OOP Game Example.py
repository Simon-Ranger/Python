"""
This is just a small and very basic text based style game to display how OOP can be implemented properly within a
script.
"""

#######################################################################################################################
#                                                  A SIMPLE GAME                                                      #
#######################################################################################################################
print(f"\n{'Building a Mini RPG Text Base Game':#^65}")


# Sets the classes and general details for the game
class GameObject:
    class_name = ""
    desc = ""
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self

    def get_desc(self): return f"{self.class_name}: {self.desc}"


class Goblin(GameObject):
    def __init__(self, name):
        self.class_name = "goblin"
        self.health = 3
        self._desc = " A foul creature"
        super().__init__(name)

    @property
    def desc(self):
        if self.health >= 3:
            return f"{self._desc}"
        elif self.health == 2:
            health_line = f"It has a wound on its knee."
        elif self.health == 1:
            health_line = f"Its left arm has been cut off!"
        elif self.health <= 0:
            health_line = f"It is dead."
        return f"{self._desc}\n{health_line}"

    @desc.setter
    def desc(self, value):
        self._desc = value


def hit(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Goblin:
            thing.health = thing.health - 1
            if thing.health <= 0:
                msg = f"You killed the goblin!"
            else:
                msg = f"You hit the {thing.class_name}"
    else:
        msg = f"There is no {noun} here."
    return msg


goblin = Goblin("Gobbly")


def examine(noun):
    if noun in GameObject.objects:
        return f"{GameObject.objects[noun].get_desc()}"
    else:
        return f"There is no {noun}"


# Function Handling of Input and Simple Parsing
# This section tries to take user input, matching the first word with the command, if found function will be called
def get_input():
    command = input("Please enter something: ").split()
    verb_word = command[0]

    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print(f"Unknown verb {verb_word}")
        return

    if len(command) >= 2:
        noun_word = command[1]
        print(f"{verb(noun_word)}")
    else:
        print(f"{verb} nothing")


def say(noun): return f"You said {noun}"


verb_dict = {
    "say": say,
    "examine": examine,
}

while True: get_input()
