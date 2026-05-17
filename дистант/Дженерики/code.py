from __future__ import annotations
from typing import TypeVar, Generic, Callable
from collections.abc import Sequence, MutableSequence
import heapq

# ЗАДАНИЕ 1: PriorityQueue<T>

T = TypeVar('T')  # Создаёт переменную типа T для использования в PriorityQueue


class PriorityQueue(Generic[T]):  # Обобщённый класс очереди с приоритетом, работающий с любым типом T
    def __init__(self, priority_func: Callable[[T], int]) -> None:
        self._priority_func = priority_func
        self._heap: list[tuple[int, int, T]] = []
        self._counter = 0

    def push(self, item: T) -> None:  # Метод добавления элемента в очередь
        priority = self._priority_func(item)
        heapq.heappush(self._heap, (-priority, self._counter, item))
        self._counter += 1

    def pop(self) -> T:  # Метод извлечения элемента с наивысшим приоритетом
        if not self._heap:
            raise IndexError("pop from empty queue")  # Выбрасывает исключение, если очередь пуста
        return heapq.heappop(self._heap)[2]

    def is_empty(self) -> bool:  # Метод проверки пустоты очереди
        return len(self._heap) == 0

    def __len__(self) -> int:  # Метод для получения размера очереди
        return len(self._heap)


# ЗАДАНИЕ 2: Иерархия Animal/Dog/Cat

class Animal:  # Базовый класс для всех животных
    def __init__(self, name: str):
        self.name = name


class Dog(Animal):  # Класс собаки
    def __init__(self, name: str):
        super().__init__(name)

    def bark(self):  # Метод, заставляющий собаку лаять
        print(f"{self.name} гавкает!")


class Cat(Animal):  # Класс кота
    def __init__(self, name: str):
        super().__init__(name)

    def meow(self):  # Метод, заставляющий кошку мяукать
        print(f"{self.name} мяукает!")


# ЗАДАНИЕ 3.1: copyAnimals

def copyAnimals(src: Sequence[Dog], dst: MutableSequence[Animal]) -> None:  # Копирует собак из src в dst
    for dog in src:  # Проходит по каждой собаке в исходном списке
        dst.append(dog)


# ЗАДАНИЕ 3.2: fillWithCats

T_contra = TypeVar('T_contra', bound=Animal, contravariant=True)


def fillWithCats(dst: MutableSequence[T_contra]) -> None:  # Очищает список и заполняет тремя котами
    dst.clear()
    dst.append(Cat("Барсик"))
    dst.append(Cat("Снежок"))
    dst.append(Cat("Рыжик"))


# ЗАДАНИЕ 3.3: safeTransfer

T_co = TypeVar('T_co', covariant=True)  # TypeVar позволяет передавать список T или его подтипов


def safeTransfer(src: MutableSequence[T_co],
                 dst: MutableSequence[T_co]) -> None:  # Переносит все элементы из src в dst, очищая src
    for item in src:
        dst.append(item)
    src.clear()


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
