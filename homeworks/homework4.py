import math
def num_input(prompt):
    while True:
        try:
            return float(input(prompt)) 
        except ValueError:
            print("Ошибка: пожалуйста, введите число.")

a = num_input("Введите первое число (a): ")
b = num_input("Введите второе число (b): ")

if a > b:
    a, b = b, a

print("Целые числа между", a, "и", b, ":")
for i in range(math.ceil(a), math.floor(b)):
    print(i)
