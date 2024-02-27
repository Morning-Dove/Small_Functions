def add(x: float, y: float) -> float:
    return x + y

def multiply(x: float, y: float) -> float:
    return x*y

def square(x: float) -> float:
    return multiply(x, x)

def add_squares(x: float, y: float) -> float:
    return add(square(x),square(y))






x = 2
y = 3

print("add", add(x,y))
print("multiply", multiply(x,y))
print("square", square(x))
print("add_squares", add_squares(x,y))
