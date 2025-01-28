#example1
a = 33
b = 200
print("Example 1:")
if b > a:
  print("b is greater than a")
print()  # Отступ после примера

#example2
a = 33
b = 33
print("Example 2:")
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
print()  # Отступ после примера

#example3
a = 200
b = 33
print("Example 3:")
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
print()  # Отступ после примера

#example4
a = 200
b = 33
print("Example 4:")
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
print()  # Отступ после примера

#example5
print("Example 5:")
if a > b: print("a is greater than b")
print()  # Отступ после примера

#example6
a = 2
b = 330
print("Example 6:")
print("A") if a > b else print("B")
print()  # Отступ после примера

#example7
a = 330
b = 330
print("Example 7:")
print("A") if a > b else print("=") if a == b else print("B")
print()  # Отступ после примера

#example8
a = 200
b = 33
c = 500
print("Example 8:")
if a > b and c > a:
  print("Both conditions are True")
print()  # Отступ после примера

#example9
a = 200
b = 33
c = 500
print("Example 9:")
if a > b or a > c:
  print("At least one of the conditions is True")
print()  # Отступ после примера

#example10
a = 33
b = 200
print("Example 10:")
if not a > b:
  print("a is NOT greater than b")
print()  # Отступ после примера

#example11
x = 41
print("Example 11:")
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
print()  # Отступ после примера

#example12
a = 33
b = 200
print("Example 12:")
if b > a:
  pass
print()  # Отступ после примера
