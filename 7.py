import math

def area_of_triangle(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def main():
    # Read the sides of the first triangle
    print("Enter the sides of the first triangle:")
    a1 = float(input("Side 1: "))
    b1 = float(input("Side 2: "))
    c1 = float(input("Side 3: "))

    # Calculate the area of the first triangle
    area1 = area_of_triangle(a1, b1, c1)
    print(f"Area of the first triangle: {area1:.2f}")

    # Read the sides of the second triangle
    print("Enter the sides of the second triangle:")
    a2 = float(input("Side 1: "))
    b2 = float(input("Side 2: "))
    c2 = float(input("Side 3: "))

    # Calculate the area of the second triangle
    area2 = area_of_triangle(a2, b2, c2)
    print(f"Area of the second triangle: {area2:.2f}")

    # Calculate the total area
    total_area = area1 + area2
    print(f"Total area enclosed by both triangles: {total_area:.2f}")

    # Calculate the contribution percentage of each triangle
    contribution1 = (area1 / total_area) * 100
    contribution2 = (area2 / total_area) * 100

    print(f"First triangle's contribution: {contribution1:.2f}%")
    print(f"Second triangle's contribution: {contribution2:.2f}%")

# Run the main function
main()
