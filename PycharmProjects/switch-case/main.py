import math

def circle():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return f"Circle -> Area: {area:.2f}, Circumference: {circumference:.2f}"

def rectangle():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    perimeter = 2 * (length + width)
    return f"Rectangle -> Area: {area:.2f}, Perimeter: {perimeter:.2f}"

def square():
    side = float(input("Enter the side length of the square: "))
    area = side ** 2
    perimeter = 4 * side
    return f"Square -> Area: {area:.2f}, Perimeter: {perimeter:.2f}"

def triangle():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    return f"Triangle -> Area: {area:.2f}"

def trapezium():
    base1 = float(input("Enter the first base of the trapezium: "))
    base2 = float(input("Enter the second base of the trapezium: "))
    height = float(input("Enter the height of the trapezium: "))
    side1 = float(input("Enter the first side of the trapezium: "))
    side2 = float(input("Enter the second side of the trapezium: "))
    area = 0.5 * (base1 + base2) * height
    perimeter = base1 + base2 + side1 + side2
    return f"Trapezium -> Area: {area:.2f}, Perimeter: {perimeter:.2f}"

def main():
    print("Select a shape to calculate:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Square")
    print("4. Triangle")
    print("5. Trapezium")

    choice = input("Enter your choice (1-5): ")

    # Emulating a switch case using a dictionary
    switch = {
        "1": circle,
        "2": rectangle,
        "3": square,
        "4": triangle,
        "5": trapezium
    }

    # Execute the corresponding function or show an error for invalid input
    result = switch.get(choice, lambda: "Invalid choice! Please select a valid option.")()
    print(result)

if __name__ == "__main__":
    main()
