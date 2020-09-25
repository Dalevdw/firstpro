import math

a=int(input("please enter a value"))
b=int(input("please enter a value"))
c=(a**2)+(b**2)
print(math.sqrt(c))

#calculating the area
area=0.5 * a * b
print(area)
print(bin(c))

#finding the largest and smallest number
numbers =[2,56,12,67,1000, 32,89,29,44,39,200,11,21]
numbers.sort()
print(numbers)
print(numbers[0])
print(numbers[12])


