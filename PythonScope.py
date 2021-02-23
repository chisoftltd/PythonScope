import os
os.system("cls")

# Python Scope
def myfunc():
    x = 250
    print(x)

myfunc()
print()

# Function Inside Function
def myfunc():
    x1 = 987
    def myinnerfunc():
        print(x1)
    myinnerfunc()

myfunc()
print()

# Global Scope
x2 = 300

def myfunc():
  print(x2)

myfunc()
x2 += 32
print(x2)
print()

# Naming Variables
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)
print()

# Global Keyword
def myfunc1():
    global x3
    x3 = 321

myfunc1()

print(x3)
print()

x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)