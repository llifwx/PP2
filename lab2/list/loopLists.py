#example1
thislist = ["apple", "banana", "cherry"]
print("Example 1:")
for x in thislist:
  print(x)
print()  

#example2
thislist = ["apple", "banana", "cherry"]
print("Example 2:")
for i in range(len(thislist)):
  print(thislist[i])
print() 

#example3
thislist = ["apple", "banana", "cherry"]
i = 0
print("Example 3:")
while i < len(thislist):
  print(thislist[i])
  i = i + 1
print()  

#example4
thislist = ["apple", "banana", "cherry"]
print("Example 4:")
[print(x) for x in thislist]
print()  
