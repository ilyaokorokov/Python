def fizz_buzz(n):
    for new in range(1, n + 1):
        if new % 3 == 0 and new % 5 == 0:  # если поставить условие в конце, а в начале на 3, то выполнит на 3 остальное пропустит
            print("FizzBuzz")
        elif new % 5 == 0:
            print("Buzz")
        elif new % 3 == 0:
            print("Fizz")
        else:
            print(new)


fizz_buzz(16)
