"""
Exercise 2 — The four scalar types and type()

The four primitive types you'll use every day:
    int     whole numbers           42, -7, 0
    float   decimal numbers         3.14, -0.5, 1.0
    str     text (in quotes)        "hello", 'world'
    bool    True or False           True, False

type(x) returns the type of any value:
    type(42)        -> <class 'int'>
    type("hello")   -> <class 'str'>
"""

# TASK 1: Create one variable of each type (int, float, str, bool).
#         Name them whatever makes sense. Print each one followed by its type.
#         Expected output should look like:
#             42 <class 'int'>
#             3.14 <class 'float'>
#             hello <class 'str'>
#             True <class 'bool'>


# TASK 2: Python has a few values that might surprise you.
#         What is the type of each of these?
#             a) type(True)
#             b) type(1.0)
#             c) type("3")
#         Print each result and note: is any of them unexpected?


# TASK 3: True and False behave like 1 and 0 in arithmetic.
#         Without running it first — what do you expect this to print?
#             print(True + True)
#             print(False + 1)
#         Then run it and see if you were right.

var1 = 42
var2 = 3.14
var3 = "hello"
var4 = True

print(var1, type(var1))
print(var2, type(var2))
print(var3, type(var3))
print(var4, type(var4))

#
print(type(True))
print(type(1.0))
print(type("3"))

#

print(True + True)
print(False + 1)