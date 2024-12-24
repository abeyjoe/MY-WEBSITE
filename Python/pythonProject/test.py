import math

def quadratic_equation(a, b, c):
    # Calculate the discriminant
    discriminant = (b ** 2) - (4 * a * c)

    if discriminant > 0:
        # Two real and distinct roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        # Two real and equal roots
        root = -b / (2 * a)
        return root, root
    else:
        # Complex roots
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

# Input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate and display the roots
roots = quadratic_equation(a, b, c)
print("Roots of the quadratic equation are:", roots)
