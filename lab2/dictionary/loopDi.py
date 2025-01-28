#example1
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
print ("")

#example2
for x in thisdict:
  print(thisdict[x])
print ("")

#example3
for x in thisdict.values():
  print(x)
print ("")

#example4
for x in thisdict.keys():
  print(x)
print ("")

#example5
for x, y in thisdict.items():
  print(x, y)