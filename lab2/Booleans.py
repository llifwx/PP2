#example1
print(10 > 9)
print(10 == 9)
print(10 < 9)
print ("")

#example2
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
print ("")

#example3
print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))
print ("")

#example4
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
print ("")

#example5
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print ("")

#example6
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#example7
def myFunction() :
  return True

print(myFunction())
print ("")

#example8
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
print ("")

#example9
x = 200
print(isinstance(x, int))