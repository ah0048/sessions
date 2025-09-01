# Primary Data types (Value Types)
# x = 10       # integer
# y = 3.14     # float
# name = "Ahmed" # string
# is_active = True # boolean


# x = 100

# result = x + y

# print(result)

# print(int(y))

# print(float(x))

# str_x = str(x)
# print(type(str_x))

# flag = False

# if flag:
#     for i in range(5):
#         print(i)


# flag = True

# string concatenation

# a = "ah"
# b = "med"

# fullname = a + b
# print(fullname)

# a = "1"
# b = "0"


# result = a + b # "10"
# result = int(result) # 10
# result -= 1
# result = result - 1

# result += 1
# result = result + 1

# result *= 1
# result = result * 1

# result /= 1
# result = result / 1

# print(result)


# ------------------------- non primary data types (Reference Types)-----------------------
a = [1, 2, 3]   # list
b = (1, 2, 3)   # tuple
c = {"key": "value"} # dict
d = {1, 2, 3}   # set

# operations on list (mutable)
a.append(4) # [1, 2, 3, 4]
x = a[-3]   #  0  1  2  3
length = len(a)
# print(a)
# print(f"length of {a}: {length}")

half_a = a[1:3]
# print(half_a)

# rev_a = a[::-1]
a.reverse() # [4, 3, 2, 1]
# print(a)
# print(rev_a)


# operations on tuple (immutable)

# tuple destructring 
# usage
# return more than one result from a function
# swap 2 variables

# l = [1, 2, 3]
# t = tuple(l)
# s = list(t)
# print(t)
# print(s)
# x = 1
# y = 2

# (x, y) = (y, x)

# print(f"x={x}, y={y}")

# def rect_op(width, length):
#     area = width * length
#     perimeter = 2 * (width + length)
#     return (area, perimeter)

# a, p = rect_op(width=10, length=20)
# print(f"rect area = {a}, rect perimeter = {p}")


# opertaion on dictionary (mutable)

# dictionary = {
#     "f_name": "ahmed",
#     "age": 25,
#     "address": "egypt"
# }

# print(dictionary["f_name"])
# print(dictionary["age"])
# print(dictionary["address"])

# dictionary["l_name"] = "khaled"
# dictionary["L_name"] = "khaled"
# print(dictionary["l_name"])
# dictionary["age"] = 30
# print(dictionary)

# opertaion on set (immutable)

# dup = [1, 2, 2, 3, 3, 4]
# unique_1 = {1}
# unique_1.add(2)

# listt = list(unique_1)
# print(unique_1)
# print(listt)
# unique = set(dup)
# unique.add(5)

# if 5 in unique:
#     print("5 exists")

# unique.remove(2)
# print(unique)


# -------------
# l = [1, 2, 3]
# d = dict(l)
# print(d)


# ---------- reference v value data types ----------------
# L = [1, 2, 3]
# new_L = L # not equal to new_L = [1, 2, 3]

# new_L.append(4)

# print(L)
# print(new_L)


# -------------- deep copy & shallow copy -----------------

import copy

# L = [1, 2, 3, [1, 2]]
#                 # x
# # L = [1, 2, 3, 1]

# new_L = copy.copy(L) # shallow copy

# new_L[0] = 2
# new_L[3][0] = 2

# print(L)
# print(new_L)

# L = [1, 2, 3, [1, 2]]
#                 # x
# # L = [1, 2, 3, 1]

# new_L = copy.deepcopy(L) # deep copy

# new_L[0] = 2
# new_L[3][0] = 2

# print(L)
# print(new_L)


# ------------- arithmetic operators -----------------
a = 10
b = 3

# print(a + b)  # 13
# print(a - b)  # 7
# print(a * b)  # 30
# print(a / b)  # 3.333...
# print(a // b) # 3 (floor division)
# import math
# print(math.ceil(a / b))  # ceil divison
# print(a % b)  # 1
# print(a ** b) # 1000 (power)

# '''
# 10 / 3 = 3 remain 1 -> result of mod %
# '''


# ------------- Comparison  operators -----------------
# print(a == b)  # False
# print(a != b)  # True
# print(a > b)   # True
# print(a <= b)  # False

# --------------- Logical Operators -----------------
x = True
y = False
# print(x and y)  # False
# print(x or y)   # True
# print(not x)    # False


# ---------------- Control Flow -------------------
# ---------------- if-else ------------------------

# num = 0
# if num > 0:
#     print("Positive")
# elif num == 0:
#     print("Zero")
# else:
#     print("Negative")


# ------------------ For Loop ------------
# for i in range(11):
#     print(i)

L = [101, 102, 103, 104]

t = (101, 102, 103, 104)

s = {101, 102, 103, 104}

d = {
    "f_name": "ahmed",
    "age": 25,
    "address": "egypt"
}

# calc_L = []
# for item in L:
#     print(item)
#     item = item / 1000
#     calc_L.append(item)

# print(L)
# print(calc_L)

# for ay_7aga in t: 
#     print(ay_7aga)

# for item in s: 
#     print(item)

# for key, value in d.items(): 
#     print(f"{key}: {value}")

# for key in d.keys(): 
#     print(f"{key}")

# for value in d.values(): 
#     print(f"{value}")

# ------------- While Loop ------------------

# count = 0
# while count < 3:
#     print(count)
#     count += 1


# ---------------- Break / Continue ---------------
# for i in range(5):
#     print(i)

# print("--------------------------")
# for i in range(5):
#     if i == 2:
#         continue  # skip 2 (skip current iteration)
#     if i == 4:
#         break     # stop loop (break the for loop)
#     print(i)


# -------------- Functions -------------------

# def greet():
#     print("Hello")
#     return 0

# def add(x, y):
#     sum = x + y
#     return sum

# sum_x_y = add(2, 3)
# print(sum_x_y)

# def greet(name):
#     if type(name) is str:
#         print(f"Hello, {name}!")
#     else:
#         return "enter a valid name"

# s = greet("Ahmed")
# print(s)


# ------------------- Default & Keyword Arguments -----------------
# # function definition
# def add(a=3, b=5):
#     return a + b

# # function call
# print(add())
# print(add(10))     # 15 (uses default b=5)
# print(add(10, 20))  # 30

# -------------- Variable Number of Arguments ------------------

# def sum_all(*args):
#     return sum(args)

# print(sum_all(1, 2, 3, 4, 5, 6, 7, 8)) # 36

# def rect_op(width, length):
#     area = width * length
#     perimeter = 2 * (width + length)
#     return (area, perimeter)

# area, peri = rect_op(10, 20)
# print(f"area={area}, perimeter={peri}")

# ------------------- Lambda Functions -----------------------

add = lambda x, y: x + y
print(add(3, 5))  # 8

square = lambda n: n ** 2
print(square(4))  # 16

