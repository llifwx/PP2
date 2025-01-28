
#example1
thisset = {"apple", "banana", "cherry"}
print("Example 1:")
thisset.remove("banana")
print(thisset)
print()  

#example2
thisset = {"apple", "banana", "cherry"}
print("Example 2:")
thisset.discard("banana")
print(thisset)
print()  

#example3
thisset = {"apple", "banana", "cherry"}
print("Example 3:")
x = thisset.pop()
print(x)
print(thisset)
print()  

#example4
thisset = {"apple", "banana", "cherry"}
print("Example 4:")
thisset.clear()
print(thisset)
print()  

#example5
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)