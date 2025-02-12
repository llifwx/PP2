def trapezoid_area(h, a, b):
    return ((a + b) * h) / 2

h = int(input("Enter height: "))
a = int(input("Enter base 1: "))
b = int(input("Enter base 2: "))

print("Trapezoid Area:", trapezoid_area(h, a, b))
