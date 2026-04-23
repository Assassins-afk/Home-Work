import math

def count_sequences(a, b):
    # Если объектов больше, чем возможных позиций — решений нет
    if a > b + 1:
        return 0
    # Считаем количество способов выбрать a позиций
    return math.comb(b + 1, a)

#Вывод
a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
print(count_sequences(a,b))