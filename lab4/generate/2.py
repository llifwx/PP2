def even_generator(n):
    for i in range(0, n + 1, 2):
        yield str(i)


n = int(input("Enter N: "))
print(",".join(even_generator(n)))
