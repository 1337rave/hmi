# Запит числа від користувача
число = float(input("Введіть число: "))

# Перевірка умови і виведення відповідного повідомлення
if число > 0:
    print("Number is positive")
elif число < 0:
    print("Number is negative")
else:
    print("Number is equal to zero")
