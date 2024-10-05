def solve(a, b, c):
    x = 7 * b + 2 * c - a
    return x

a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
c = float(input("Введите значение c: "))

result = solve(a, b, c)

print("x = " + str(result))