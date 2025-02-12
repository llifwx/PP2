def div34(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


n = int(input("Enter N: "))
for num in div34(n):
    print(num, end=" ")
print()
