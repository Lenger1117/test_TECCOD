"""2. Написать функцию, которая принимает на вход два целых числа (минимум и максимум) и возвращает список всех простых чисел в заданном диапазоне."""

def numbers_range():
    a = int(input("Введите минимальное заданное число: "))
    b = int(input("Введите максимально заданное число: "))
    lst = []
    for num in range(a, b):
        count = 0
        delitel = 2
        while delitel < num:
            if num % delitel == 0:
                count += 1
            delitel += 1
        if count == 0:
            lst.append(num)
    print(lst)

numbers_range()