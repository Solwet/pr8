def num_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: пожалуйста, введите целое число.")

a = num_input("Введите первое число (a): ")
b = num_input("Введите второе число (b): ")

print("Целые числа между", a, "и", b, ":")
for i in range(a + 1, b):
    print(i)