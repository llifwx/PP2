#example1
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
print("Example 1:")
set3 = set1.union(set2)
print(set3)
print()  

#example2
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
print("Example 2:")
set3 = set1 | set2
print(set3)
print()  

#example3
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
print("Example 3:")
myset = set1.union(set2, set3, set4)
print(myset)
print()  

#example4
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
print("Example 4:")
myset = set1 | set2 | set3 | set4
print(myset)
print()  

#example5
x = {"a", "b", "c"}
y = (1, 2, 3)
print("Example 5:")
z = x.union(y)
print(z)
print()  

#example6
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
print("Example 6:")
set1.update(set2)
print(set1)
print()  

#example7
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print("Example 7:")
set3 = set1.intersection(set2)
print(set3)
print()  

#example8
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print("Example 8:")
set3 = set1 & set2
print(set3)
print()  

#example9
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print("Example 9:")
set1.intersection_update(set2)
print(set1)
print()  

#example10
set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
print("Example 10:")
set3 = set1.intersection(set2)
print(set3)
print()  

#example11
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print("Example 11:")
set3 = set1.difference(set2)
print(set3)
print()  

#example12
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print("Example 12:")
set3 = set1 - set2
print(set3)
print()  

#example13
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print("Example 13:")
set1.difference_update(set2)
print(set1)
print() 

#example14
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print("Example 14:")
set3 = set1.symmetric_difference(set2)
print(set3)
print() 

#example15
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print("Example 15:")
set3 = set1 ^ set2
print(set3)
print() 

#example16
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print("Example 16:")
set1.symmetric_difference_update(set2)
print(set1)
print()  
