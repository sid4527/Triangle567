def classifyTriangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Not a triangle"

    if a == b == c:
        return "Equilateral"

    if a == b or b == c or a == c:
        if a * a + b * b == c * c:
            return "Isosceles and Right"
        return "Isosceles"

    if a * a + b * b == c * c:
        return "Scalene and Right"

    return "Scalene"

# For testing
if __name__ == "__main__":
    a = int(input("Input the length for side a: "))
    b = int(input("Input the length for side b: "))
    c = int(input("Input the length for side c: "))
    triangle_result = classifyTriangle(a, b, c)
    print(f"This is {triangle_result}.")