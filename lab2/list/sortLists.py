#example1
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#example2
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#example3
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#example4
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#example5
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#example6
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#example7
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#example8
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)