#example1
fruits = ["apple", "banana", "cherry"]
print("Example 1:")
for x in fruits:
  print(x)
print()  # Отступ после примера

#example2
print("Example 2:")
for x in "banana":
  print(x)
print()  # Отступ после примера

#example3
fruits = ["apple", "banana", "cherry"]
print("Example 3:")
for x in fruits:
  print(x)
  if x == "banana":
    break
print()  # Отступ после примера

#example4
fruits = ["apple", "banana", "cherry"]
print("Example 4:")
for x in fruits:
  if x == "banana":
    break
  print(x)
print()  # Отступ после примера

#example5
fruits = ["apple", "banana", "cherry"]
print("Example 5:")
for x in fruits:
  if x == "banana":
    continue
  print(x)
print()  # Отступ после примера

#example6
print("Example 6:")
for x in range(6):
  print(x)
print()  # Отступ после примера

#example7
print("Example 7:")
for x in range(2, 6):
  print(x)
print()  # Отступ после примера

#example8
print("Example 8:")
for x in range(2, 30, 3):
  print(x)
print()  # Отступ после примера

#example9
print("Example 9:")
for x in range(6):
  print(x)
else:
  print("Finally finished!")
print()  # Отступ после примера

#example10
print("Example 10:")
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
print()  # Отступ после примера

#example11
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
print("Example 11:")
for x in adj:
  for y in fruits:
    print(x, y)
print()  # Отступ после примера

#example12
print("Example 12:")
for x in [0, 1, 2]:
  pass
print()  # Отступ после примера
