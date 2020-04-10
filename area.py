import  math

user_radius = float(input("Enter the radius of the circle: "))

def area(radius):
    return math.pi * radius * radius

print(f"The area of the circle with radius {user_radius} is {area(user_radius)}")
