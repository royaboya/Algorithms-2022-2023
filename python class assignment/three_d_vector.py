import math


class ThreeDVector:
    def __init__(self, x, y, z):
        # Do things here.
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        # Do things here.
        return f"<{self.x},{self.y},{self.z}>"

    def __add__(self, other):
        # Do things here.
        return ThreeDVector(self.x + other.x, self.y + other.y, self.z + other.z)

    def magnitude(self):
        # Fill in code here.
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)


def main():
    # Examples:
    v1 = ThreeDVector(3, 4, 12)
    v2 = ThreeDVector(1, 0, -1)
    print(v1 + v2)  # output: <4, 4, 11>
    print(v1.magnitude())  # output: 13.0


if __name__ == "__main__":
    main()