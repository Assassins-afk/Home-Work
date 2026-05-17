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

def safeTransfer(src: MutableSequence[T_co], dst: MutableSequence[T_co]) -> None:  # Переносит все элементы из src в dst, очищая src
    for item in src:
        dst.append(item)
    src.clear()

# ТЕСТЫ

# Проверка 1: с List[Animal]
animals: list[Animal] = [Dog("Шарик")]
fillWithCats(animals)  # Очищает animals и заполняет тремя котами: теперь [Cat, Cat, Cat]

# Проверка 2: с List[Cat]
cats: list[Cat] = [Cat("Барсик")]
fillWithCats(cats)  # Контравариантность позволяет передать List[Cat] вместо List[Animal]

# Проверка safeTransfer
dogs: list[Dog] = [Dog("Шарик"), Dog("Бобик")]
animals2: list[Animal] = [Cat("Мурка")]
safeTransfer(dogs, animals2)  # Переносит собак в animals2: dogs пуст, animals2 содержит [Cat, Dog, Dog]

# Проверка классов
my_dog = Dog(name="Белка")
my_dog.bark()

my_cat = Cat(name="Мурка")
my_cat.meow()
