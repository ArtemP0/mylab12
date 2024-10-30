import math

x_min = float(input("Введіть початкову межу x: "))
x_max = float(input("Введіть кінцеву межу x: "))
step = 0.1
x = x_min

def f(x):
    inner_value = abs(-x**2 + 6)
    if inner_value > 0:
        return 5 * abs(math.log(inner_value))
    else:
        return None
    
while x <= x_max:
    if f(x) is not None:
        print(f"x = {x:.1f}, f(x) = {f(x):.3f}")
    else:
        print(f"x = {x:.1f}, f(x) не визначено")
    x += step
