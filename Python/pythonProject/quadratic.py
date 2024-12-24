# Import math Library
import math

# Return the square root of different numbers
#print (math.sqrt(9))
#print (cmath.sqrt(9))

root1 = float
root2 = float
discriminant = float

print("Quadratic Equation Calculator...")
print(" ")

a = int(input("Enter a:  "))
b = int(input("Enter b:  "))
c = int(input("Enter c:  "))

discriminant = (b ** 2) -(4 * a * c)

root1 = (-b + math.sqrt(discriminant)) / (2 * a)
root2 = (-b - math.sqrt(discriminant)) / (2 * a)

print(" ")
answer = "Answer = " + str(root1) + " or " + str(root2)
print(answer)
