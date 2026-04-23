import math

def count_sequences(a, b):
    if a > b + 1:
        return 0
    return math.comb(b + 1, a)

# Пример использования
a = int(input("Введите количество нулей (a): "))
b = int(input("Введите количество единиц (b): "))

result = count_sequences(a, b)
print(f"Количество последовательностей: {result}")