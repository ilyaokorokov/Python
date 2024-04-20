def month_to_season(month):
        if month in (1, 2, 12):
            print("Зима")
        elif month in (3, 4, 5):
            print("Весна")
        elif month in (6, 7, 8):
            print("Лето")
        else:
            print("Осень")


month_to_season(9)


data = int(input("Введите месяц: "))


def mont_season(data):
    if data < 1 or data > 12:
        print("Укажите значение от 1 до 12")
    else:
        if data in (1, 2, 12):
            print("Зима")
        elif data in (3, 4, 5):
            print("Весна")
        elif data in (6, 7, 8):
            print("Лето")
        else:
            print("Осень")


mont_season(data)
