def inf_input(x):
    while True:
        try:
            return int(input(x))
        except ValueError:
            print("Ошибка: пожалуйста, введите целое число.")


a = inf_input("Введите первое число (a): ")
b = inf_input("Введите второе число (b): ")


print("Целые числа между", a, "и", b, ":")
for i in range(a + 1, b):
    print(i)
