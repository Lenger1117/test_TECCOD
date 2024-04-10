"""1. Написать функцию, которая принимает на вход список целых чисел и возвращает новый список, содержащий только уникальные элементы из исходного списка."""
def unique_list(numbers):
    unique = []
    for i in numbers:
        if i not in unique:
            unique.append(i)
    return unique

un_list = list(input('Введите числа без знаков между ними: '))
print(unique_list(un_list))