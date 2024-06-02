import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        return None

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

roots = solve_quadratic(a, b, c)
if roots:
    if isinstance(roots, tuple):
        print(f"The roots are {roots[0]} and {roots[1]}")
    else:
        print(f"The root is {roots}")
else:
    print("No real roots")