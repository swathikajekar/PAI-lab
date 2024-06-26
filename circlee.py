import math

def calculate_area(radius):
    """Calculate the area of a circle given its radius."""
    return math.pi * radius * radius

def main():
    # Read user input
    radius = float(input("Enter the radius of the circle: "))
    
    # Calculate the area
    area = calculate_area(radius)
    
    # Print the result
    print(f"The area of the circle with radius {radius} is {area:.2f}")

if __name__ == "__main__":
    main()
