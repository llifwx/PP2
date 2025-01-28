#example1
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#example2
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#example3
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#example4
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)