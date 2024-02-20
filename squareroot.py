import math

x=float(input("Enter the number: "))
tolerance=0.000001
estimate=1.0

while True:
    estimate=(estimate+x/estimate)/2
    difference=abs(x-estimate**2)
    if difference<=tolerance:
        break

print("Program estimate4:",estimate)
print("Python's estimate:",math.sqrt(x))