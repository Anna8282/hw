import math
import os


class Figure:
    def dimension(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    def square(self):
        raise NotImplementedError

    def square_surface(self):
        return None

    def square_base(self):
        return None

    def height(self):
        return None

    def volume(self):
        return self.square()


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
        if not self.is_valid():
            raise ValueError("Трикутник із такими сторонами не існує")

    def is_valid(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a

    def dimension(self):
        return 2

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def dimension(self):
        return 2

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def dimension(self):
        return 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def square(self):
        return math.pi * self.radius ** 2


class Ball(Figure):
    def __init__(self, radius):
        self.radius = radius

    def dimension(self):
        return 3

    def square_surface(self):
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        return (4 / 3) * math.pi * self.radius ** 3


class Cone(Figure):
    def __init__(self, radius, height):
        self.radius, self.height = radius, height

    def dimension(self):
        return 3

    def square_surface(self):
        l = math.sqrt(self.radius ** 2 + self.height ** 2)
        return math.pi * self.radius * l

    def square_base(self):
        return math.pi * self.radius ** 2

    def volume(self):
        return (1 / 3) * self.square_base() * self.height


def read_shapes_from_file(file_name):
    max_shape = None
    max_measure = -1

    try:
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if not parts:
                    continue
                shape_type, *params = parts
                params = list(map(float, params))

                shape = None
                if shape_type == "Triangle" and len(params) == 3:
                    shape = Triangle(*params)
                elif shape_type == "Rectangle" and len(params) == 2:
                    shape = Rectangle(*params)
                elif shape_type == "Circle" and len(params) == 1:
                    shape = Circle(*params)
                elif shape_type == "Ball" and len(params) == 1:
                    shape = Ball(*params)
                elif shape_type == "Cone" and len(params) == 2:
                    shape = Cone(*params)

                if shape:
                    measure = shape.volume()
                    if measure > max_measure:
                        max_measure = measure
                        max_shape = shape
    except (FileNotFoundError, ValueError):
        print(f"Помилка при зчитуванні файлу: {file_name}")

    return max_shape, max_measure


def read(filename):
    file = open(filename, "r")
    # content = file.read()
    lines = file.readlines()
    file.close()
    return lines


if __name__ == "__main__":
    input_files = ["input01.txt", "input02.txt", "input03.txt"]
    overall_max_shape, overall_max_measure = None, -1

    for file in input_files:
        shape, measure = read_shapes_from_file(file)
        if measure > overall_max_measure:
            overall_max_measure = measure
            overall_max_shape = shape

    if overall_max_shape:
        print(f"Фігура з найбільшою мірою: {overall_max_shape.__class__.__name__} ({overall_max_measure})")
    else:
        print("Жодної коректної фігури не знайдено")