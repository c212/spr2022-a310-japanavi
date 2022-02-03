class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def length(self):
        return self.a.distanceTo(self.b)


class Tree:
    def __init__(self, value, left, right):
        (self.value, self.left, self.right) = (value, left, right)

    def show(self):
        if self.left == None:
            left = " . "
        else:
            left = self.left.show()
        if self.right == None:
            right = " . "
        else:
            right = self.right.show()
        # return "(" + left + " " + str(self.value) + " " + right + ")"
        return "(" + str(self.value) + " " + left + " " + right + ")"


class LinkedList:
    def __init__(self, value, rest):
        self.first = value
        self.rest = rest

    def show(self):
        if self.rest == None:
            return str(self.first) + " ."
        else:
            return str(self.first) + " " + self.rest.show()


class Queue:
    def __init__(self):
        self.data = None

    def show(self):
        if self.data == None:
            return "front: ."
        else:
            return "front: " + self.data.show()

    def add(self, value):
        if self.data == None:
            self.data = LinkedList(value, None)
        else:
            morgan = self.data
            while morgan.rest != None:
                morgan = morgan.rest
            morgan.rest = LinkedList(value, None)


class MyList(LinkedList):
    def __init__(self, value, rest):
        super().__init__(value, rest)

    def addToEnd(self, value):
        if self.rest == None:
            return MyList(self.first, MyList(value, None))
        else:
            return MyList(self.first, self.rest.addToEnd(value))


def main():
    print("Tree:")
    a = Tree(5, None, None)
    print(a.show())

    a = Tree(1, a, None)
    print(a.show())

    a = Tree(2, Tree(4, None, None), a)
    print(a.show())

    print("-------------------------")

    print("LinkedList:")
    a = LinkedList(9, LinkedList(-2, None))
    print(a.show())  # 9 -2 .

    print("-------------------------")

    print("Queue:")
    a = Queue()
    print(a.show())  # front: .
    a.add(3)
    a.add(5)
    a.add(-1)
    print(a.show())  # front: 3 5 -1 .

    print("-------------------------")

    print("My List:")
    a = MyList(3, None)
    print(a.show())  # 3 .
    a = a.addToEnd(4)
    a = a.addToEnd(5)
    a = a.addToEnd(6)
    print(a.show())  # 3 4 5 6 .


if __name__ == "__main__":
    main()
