#=============ТЕСТЫ=================================
if __name__ == "__main__":
    print("РЕЗУЛЬТАТЫ РАБОТЫ КОДА")
    print()

    # Тесты PriorityQueue (2 теста)
    print("--- PriorityQueue ---")

    print("Тест 1: Порядок извлечения и работа с разными приоритетами")
    pq = PriorityQueue[int](priority_func=lambda x: x)
    pq.push(3)
    pq.push(1)
    pq.push(4)
    pq.push(-10)
    print("  Добавлены: 3, 1, 4, -10")
    print("  Порядок извлечения:", [pq.pop() for _ in range(4)])
    print("  Ожидаемый порядок: [4, 3, 1, -10]")
    print()

    print("Тест 2: Пустая очередь, исключения и равные приоритеты")
    pq = PriorityQueue[str](priority_func=lambda x: len(x))
    print("  Пустая очередь is_empty:", pq.is_empty())
    try:
        pq.pop()
    except IndexError as e:
        print("  Исключение при pop:", e)

    pq.push("aaa")
    pq.push("bbb")
    pq.push("cc")
    print("  Добавлены строки 'aaa', 'bbb', 'cc'")
    print("  Порядок извлечения:", [pq.pop() for _ in range(3)])
    print("  Длина после извлечения:", len(pq))
    print()

    # Тесты иерархии Animal (2 теста)
    print("--- Иерархия Animal/Dog/Cat ---")

    print("Тест 3: Создание объектов и проверка типов")
    dog = Dog("Шарик")
    cat = Cat("Мурка")
    print("  Dog('Шарик') isinstance Animal:", isinstance(dog, Animal))
    print("  Cat('Мурка') isinstance Animal:", isinstance(cat, Animal))
    print("  Имя собаки:", dog.name)
    print("  Имя кошки:", cat.name)
    print()

    print("Тест 4: Методы bark и meow с полиморфизмом")
    animals: list[Animal] = [Dog("Бобик"), Cat("Снежок")]
    for animal in animals:
        if isinstance(animal, Dog):
            print(f"  {animal.name} говорит: ", end="")
            animal.bark()
        elif isinstance(animal, Cat):
            print(f"  {animal.name} говорит: ", end="")
            animal.meow()
    print()

    # Тесты copyAnimals (2 теста)
    print("--- copyAnimals ---")

    print("Тест 5: Копирование в пустой и непустой списки")
    src_dogs = [Dog("Бобик"), Dog("Тузик")]
    dst_animals: list[Animal] = []
    copyAnimals(src_dogs, dst_animals)
    print("  Копирование в пустой список:", [f"{type(a).__name__}('{a.name}')" for a in dst_animals])

    dst_animals = [Cat("Мурка")]
    copyAnimals(src_dogs, dst_animals)
    print("  Копирование в непустой список:", [f"{type(a).__name__}('{a.name}')" for a in dst_animals])
    print()

    print("Тест 6: Исходный список не изменяется")
    src_dogs = [Dog("Рекс"), Dog("Цезарь")]
    original_len = len(src_dogs)
    dst_animals: list[Animal] = []
    copyAnimals(src_dogs, dst_animals)
    print("  Исходный список после копирования:", [f"Dog('{d.name}')" for d in src_dogs])
    print("  Длина src не изменилась:", len(src_dogs) == original_len)
    print("  Длина dst:", len(dst_animals))
    print()

    # Тесты fillWithCats (2 теста)
    print("--- fillWithCats ---")

    print("Тест 7: Заполнение котами и замена существующих")
    animals: list[Animal] = [Dog("Старый пёс")]
    print("  До заполнения:", [f"{type(a).__name__}('{a.name}')" for a in animals])
    fillWithCats(animals)
    print("  После заполнения:", [f"{type(a).__name__}('{a.name}')" for a in animals])
    print("  Все коты:", all(isinstance(a, Cat) for a in animals))
    print()

    print("Тест 8: Повторное заполнение уже кошачьего списка")
    animals = [Cat("Мурка"), Cat("Барсик")]
    print("  До заполнения:", [f"Cat('{a.name}')" for a in animals])
    fillWithCats(animals)
    print("  После заполнения:", [f"Cat('{a.name}')" for a in animals])
    print("  Длина списка:", len(animals))
    print()

    # Тесты safeTransfer (2 теста)
    print("--- safeTransfer ---")

    print("Тест 9: Базовый перенос и перенос в пустой список")
    src = [Dog("Шарик"), Dog("Белка")]
    dst: list[Animal] = [Cat("Мурка")]
    print("  До переноса src:", [f"{type(a).__name__}('{a.name}')" for a in src])
    print("  До переноса dst:", [f"{type(a).__name__}('{a.name}')" for a in dst])
    safeTransfer(src, dst)
    print("  После переноса src:", src)
    print("  После переноса dst:", [f"{type(a).__name__}('{a.name}')" for a in dst])

    src = [Dog("Бобик"), Cat("Снежок")]
    dst: list[Animal] = []
    safeTransfer(src, dst)
    print("  Перенос в пустой список:", [f"{type(a).__name__}('{a.name}')" for a in dst])
    print()

    print("Тест 10: Граничные случаи и полиморфизм")
    # Перенос из пустого списка
    src: list[Animal] = []
    dst = [Cat("Мурка")]
    safeTransfer(src, dst)
    print("  Перенос из пустого списка (dst не изменился):",
          [f"{type(a).__name__}('{a.name}')" for a in dst])

    # Полиморфный перенос
    src = [Dog("Пёс"), Cat("Кот"), Dog("Собака")]
    dst: list[Animal] = []
    safeTransfer(src, dst)
    print("  Полиморфный перенос:", [f"{type(a).__name__}('{a.name}')" for a in dst])
    print("  Типы в dst:", [type(a).__name__ for a in dst])
    print()