import math

def dtor(degrees):
    radian = degrees * (math.pi / 180)
    print("Output radian:", radian)

degrees = int(input("Input degree: "))
dtor(degrees)