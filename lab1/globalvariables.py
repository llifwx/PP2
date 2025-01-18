#example1
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#example2
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#example3
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#example4
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)