x = int(input("Введите сумму вклада в рублях: "))
y = int(input("Введите срок вклада в годах: "))


def bank(x, y):
    z = 0.1
    for new in range(y + 1):
        x += x * z
    return x


summa = bank(x, y)
print("Сумма на счету спустя", y, "лет будет: ", round(summa, 4), "рублей")
