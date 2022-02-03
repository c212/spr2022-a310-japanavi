from creature import Creature


class Dog(Creature):
    def __init__(self, name):
        super().__init__(name)

    def makeSound(self):
        return ": woof."


def main():
    dog = Dog("Josh")
    print(dog.talk())


if __name__ == "__main__":
    main()
