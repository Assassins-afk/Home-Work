def fibonacci(n, a=0, b=1, result=None):
    # Создаём список для результата при первом вызове
    if result is None:
        result = []
    # Останавливаем рекурсию, если число превысило N
    if a > n:
        return result
    # Добавляем текущее число в список
    result.append(a)
    # Рекурсивно вызываем функцию для следующего числа
    return fibonacci(n, b, a + b, result)
# Вывод
N = int(input('Введите число: '))
print(fibonacci(N))