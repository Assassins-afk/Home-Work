def print_matrix(matrix):
    #Функция 1: вывести матрицу
    for row in matrix:
        for element in row:
            print(f"{element:4d}", end=" ")
        print()


def sum_of_digits(num):
    #Функция 2: находит сумму цифр целого числа
    # Берем абсолютное значение для корректной работы с отрицательными числами
    num = abs(num)
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total


def count_numbers_with_sum_less_than(matrix, sum0):
    #Функция 3: на побочной диагонали ищет количество чисел,
    #у которых сумма цифр меньше заданной SUM0
    count = 0
    n = len(matrix)  # размерность квадратной матрицы

    # Проходим по побочной диагонали
    for i in range(n):
        num = matrix[i][n - 1 - i]
        if sum_of_digits(num) < sum0:
            count += 1

    return count


def main():
    # Определяем матрицу при объявлении
    matrix = [
        [2015, 123, 456, 789],
        [111, 222, 333, 444],
        [555, 666, 777, 888],
        [999, 100, 200, 300]
    ]

    print("Исходная матрица:")
    print_matrix(matrix)

    # Вводим SUM0
    try:
        sum0 = int(input("\nВведите значение SUM0: "))
    except ValueError:
        print("Ошибка: введите целое число!")
        return

    # Вызываем третью функцию и выводим результат
    result = count_numbers_with_sum_less_than(matrix, sum0)
    print(f"\nКоличество чисел на побочной диагонали, "
          f"сумма цифр которых меньше {sum0}: {result}")


if __name__ == "__main__":
    main()