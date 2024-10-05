def inf_input(x):
    while True:
        try:
            # Запрашиваем ввод у пользователя
            return int(input(x))
        except ValueError:
            # Если пользователь ввел не число, выводим сообщение об ошибке
            print("Ошибка: пожалуйста, введите целое число.")

# Запрашиваем у пользователя два числа
a = inf_input("Введите первое число (a): ")
b = inf_input("Введите второе число (b): ")


print("Целые числа между", a, "и", b, ":")
for i in range(a + 1, b):
    print(i)
