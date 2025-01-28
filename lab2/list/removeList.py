#example1
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#example2
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#example3
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#example4
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#example5
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#example6
thislist = ["apple", "banana", "cherry"]
del thislist

#example7
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)