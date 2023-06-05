# Задача №35.
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def naturalNumber (n):
    if n %1 == 0 and n %n == 0:
        return 'Yes'
    else:
        return 'No'

n = int(input('Введите число: '))
print(naturalNumber(n))
