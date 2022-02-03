class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def distanceTo(self, otherPoint) -> float:
        dx = self.x - otherPoint.x
        dy = self.y - otherPoint.y

        return (dx ** 2 + dy ** 2) ** 0.5


class Line(Point):
    def __init__(self, pt1: Point, pt2: Point) -> None:
        self.pt1 = pt1
        self.pt2 = pt2

    def __str__(self) -> str:
        return f"{self.pt1} <-> {self.pt2}"

    def length(self) -> float:
        return ((self.pt1.x - self.pt2.x) ** 2 + (self.pt1.y - self.pt2.y) ** 2) ** 0.5


class Triangle:
    pass


class Sequence:
    pass


class BinaryTree:
    pass


def test_point():
    a = Point(3, 2)
    b = Point(-1, 5)
    print(a)  # prints: (3, 2)
    print(f"I have two point objects: {a} {b}")
    # I have two point objects: (3, 2) (-1, 5)
    howFar = a.distanceTo(b)
    print(howFar)  # prints 5

    a = Point(0, 0)
    b = Point(1, 1)
    print(f"Distance from {a} to {b} is: {a.distanceTo(b):.4f}")


def test_line():
    a = Point(3, 2)
    b = Point(-1, 5)

    line = Line(a, b)
    print(line)
    print(f"{line.length() = }")


def main():
    print("Testing Point Class:")
    test_point()

    print("\nTesting Line Class:")
    test_line()


if __name__ == "__main__":
    main()
