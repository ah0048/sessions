class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self, speed):
        print(f"{self.brand} car is driving at speed {speed} km/hr")

# car1 = Car("Toyota", "Red")
# car1.drive(100)

# car2 = Car("Audi", "Black")
# car2.drive(120)

# a = str("ali")
# print(a)
# print(type(Car))
# print(type(str))

# #part 1
# part_name = "jkguij"
# part_d1 = 10
# part_d2 = 20
# part_cost = 100
# part_density = 1000


# #part 2
# part2_name = "jkguij"
# part2_d1 = 10
# part2_d2 = 20
# part2_cost = 100
# part2_density = 1000

# # part 3
# part2_name = "jkguij"
# part2_d1 = 10
# part2_d2 = 20
# part2_cost = 100
# part2_density = 1000

# class Part:
#     def __init__(self, d1, d2, cost, density ):
#         self.d1 = d1
#         self.d2 = d2
#         self.cost = cost
#         self.density = density

# part1 = Part(100, 200)


# print(part1.d1)

class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def honk(self):
        print("Car honks!")

# c = Car()
# c.move()
# c.honk()


# class Dog:
#     def sound(self): 
#         return "Woof"

# class Cat:
#     def sound(self): 
#         return "Meow"

# for animal in [Dog(), Cat()]:
#     print(animal.sound())


# class Example:
#     def __init__(self):
#         self.public = "I’m public"
#         self._protected = "I’m protected"
#         self.__private = "I’m private"

# x = Example()
# print(x.public)
# print(x._protected)
# print(x.__private)

# class Employee:
#     def __init__(self, salary):
#         self.__salary = salary

#     # getter
#     @property
#     def salary(self):
#         return self.__salary

#     #setter
#     @salary.setter
#     def salary(self, value):
#         if value < 0:
#             raise ValueError("Salary cannot be negative")
#         self.__salary = value

# e = Employee(5000)
# # print(e.salary)      # getter
# # e.salary = 6000      # setter
# e.salary = -1000
# # e.salary(-1000)
# print(e.salary)

# salary = 1000
# if salary > 0:
#     e.salary = salary


class MathUtils:
    factor = 10   # static attribute (class attribute)

    def __init__(self, value):
        self.value = value

    def instance_method(self):                   # instance is object
        return self.value * MathUtils.factor

    @classmethod
    def class_method(cls, val):         # cls is shorthand for class
        return val * cls.factor         # 10 * 10

    @staticmethod
    def static_method(x, y):
        return x + y


m = MathUtils(100)

print(m.instance_method())

print(MathUtils.class_method(10))


print(MathUtils.static_method(2, 3))
