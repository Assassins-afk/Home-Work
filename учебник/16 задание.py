# 1. Функция для поиска min и max в одномерном массиве
def find_min_max(arr):
    minimum = min(arr)
    maximum = max(arr)
    return minimum, maximum

# 2. Функция для поиска min и max во всей матрице с помощью первой функции
def find_min_max_in_matrix(matrix):
    # Преобразуем матрицу в одномерный список
    all_elements = [elem for row in matrix for elem in row]
    # Используем первую функцию
    return find_min_max(all_elements)

# Основная часть программы
def main():
    # Определение матрицы при объявлении
    matrix = [
        [12, 5, 8],
        [3, 20, 7],
        [1, 4, 15]
    ]

    # Вывод матрицы
    print("Матрица:",'\n',matrix)


    # Поиск min и max во всей матрице
    min_val, max_val = find_min_max_in_matrix(matrix)

    # Вывод результата
    print(f"\nНаименьший элемент в матрице: {min_val}")
    print(f"Наибольший элемент в матрице: {max_val}")

# Запуск программы
if __name__ == "__main__":
    main()