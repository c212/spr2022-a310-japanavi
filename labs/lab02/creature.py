class Creature:
    def __init__(self, name):
        self.name = name
        print("Creature " + self.name + " created.")

    def talk(self) -> str:
        return (
            "My name is "
            + self.name
            + " and I am a "
            + type(self).__name__
            + self.makeSound()
        )

    def makeSound(self):
        return ""


def main():
    creature = Creature("Josh")
    print(creature.talk())


if __name__ == "__main__":
    main()
