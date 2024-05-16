a = int(input("Введите год: "))


def is_year_leap(a):
    if (a % 4 == 0):
        print("Год високосный")
        return True
    elif (a % 400 == 0):
        print("Год високосный")
        return True
    elif (a % 100 == 0):
        print("Год не високосный")
        return False
    else:
        print("Год не високосный")
        return False


new = is_year_leap(a)

print("год ", a, ":",  new)
