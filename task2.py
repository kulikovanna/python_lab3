class Rectangle:
    def __init__(self, id, width, height, x, y):
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота прямоугольника должны быть больше нуля")
        self.id = id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        return self.width * self.height

    def is_intersect(self, other):
        # проверка пересечения прямоугольников
        if (self.x < other.x + other.width and self.x + self.width > other.x and
                self.y < other.y + other.height and self.y + self.height > other.y):
            return True
        else:
            return False


class Quad:
    def __init__(self, id, side_length, x, y):
        if side_length <= 0:
            raise ValueError("Длина стороны квадрата должна быть больше нуля")
        self.id = id
        self.side_length = side_length
        self.x = x
        self.y = y

    def area(self):
        return self.side_length ** 2

    def is_intersect(self, other):
        # проверка пересечения квадратов
        if (self.x < other.x + other.side_length and self.x + self.side_length > other.x and
                self.y < other.y + other.side_length and self.y + self.side_length > other.y):
            return True
        else:
            return False


# экземпляры
try:
    rect1 = Rectangle("rect1", 4, 5, 0, 0)
    rect2 = Rectangle("rect2", 3, 6, 2, 2)

    quad1 = Quad("quad1", 4, 2, 2)
    quad2 = Quad("quad2", 3, 7, 7)
except ValueError as e:
    print("Ошибка при создании объекта:", e)
else:
    # сравнение прямоугольников
    print("Сравнение прямоугольников:")
    print("Площадь прямоугольника 1:", rect1.area())
    print("Площадь прямоугольника 2:", rect2.area())
    if rect1.area() < rect2.area():
        print("Площадь прямоугольника 1 меньше площади прямоугольника 2")
    elif rect1.area() > rect2.area():
        print("Площадь прямоугольника 1 больше площади прямоугольника 2")
    else:
        print("Площади прямоугольников 1 и 2 равны")

    if rect1.is_intersect(rect2):
        print("Прямоугольник 1 и Прямоугольник 2 пересекаются")
    else:
        print("Прямоугольник 1 и Прямоугольник 2 не пересекаются")

    # сравнение квадратов
    print("\nСравнение квадратов:")
    print("Площадь квадрата 1:", quad1.area())
    print("Площадь квадрата 2:", quad2.area())
    if quad1.area() < quad2.area():
        print("Площадь квадрата 1 меньше площади квадрата 2")
    elif quad1.area() > quad2.area():
        print("Площадь квадрата 1 больше площади квадрата 2")
    else:
        print("Площади квадратов 1 и 2 равны")

    if quad1.is_intersect(quad2):
        print("Квадрат 1 и Квадрат 2 пересекаются")
    else:
        print("Квадрат 1 и Квадрат 2 не пересекаются")
