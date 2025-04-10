# Функція для обчислення квадрата числа
def square(x):
    return x * x

if __name__ == "__main__":
    n = int(input("Введіть число: "))
    print(f"Квадрат: {square(n)}")
