import random

menu = int(input('0(Выход);\n1(Начать игру).\nВведите: '))
if menu == 1:
    class Race:
        """Базовый класс для всех рас"""

        def __init__(self, health, damage):
            self.health = health
            self.max_health = health
            self.damage = damage

        def take_damage(self, amount):
            """Метод получения урона"""
            self.health -= amount
            if self.health < 0:
                self.health = 0
            return self.health

        def is_alive(self):
            """Проверка, жив ли персонаж"""
            return self.health > 0

        def special_attack_effect(self, enemy):
            """Специальный эффект при атаке (переопределяется в дочерних классах)"""
            pass

        def calculate_damage(self):
            """Расчёт урона (переопределяется в дочерних классах)"""
            return random.randint(1, self.damage)

        def attack(self, enemy):
            """метод атаки для всех рас"""
            # Расчёт урона
            damage_dealt = self.calculate_damage()

            # Нанесение урона
            enemy.take_damage(damage_dealt)
            print(f"⚔️ {self.race_name} атакует и наносит {damage_dealt} урона!")

            # Применяем специальный эффект расы
            self.special_attack_effect(enemy)

            return damage_dealt


    # раса Орк
    class Orc(Race):
        def __init__(self, health, damage):
            super().__init__(health, damage)
            self.race_name = 'Орк'
            self.base_damage = damage
            self.berserk_activated = False

        def describe(self):
            print(f"\nРаса: {self.race_name}")
            print(f"Здоровье: {self.health}/{self.max_health}")
            print(f"Атака: {self.damage}")

        def activate_berserk(self):
            """Активация режима Берсерка"""
            bonus = random.randint(45, 60)
            self.damage += bonus
            self.berserk_activated = True
            print(f"🔥 ОРК ВПАДАЕТ В ЯРОСТЬ! Атака увеличена на {bonus}!")
            print(f"💥 Новая атака: {self.damage}")

        def take_damage(self, amount):
            """Переопределяем получение урона для мгновенной активации берсерка"""
            self.health -= amount
            if self.health < 0:
                self.health = 0

            # Активируем берсерк сразу при падении здоровья
            if 0 < self.health <= 10 and not self.berserk_activated:
                self.activate_berserk()

            return self.health

        def reset_for_battle(self):
            """Сброс баффов перед новым боем"""
            self.damage = self.base_damage
            self.berserk_activated = False


    # раса Гном
    class Dwarf(Race):
        def __init__(self, health, damage):
            super().__init__(health, damage)
            self.race_name = 'Гном'

        def describe(self):
            print(f"\nРаса: {self.race_name}")
            print(f"Здоровье: {self.health}/{self.max_health}")
            print(f"Атака: {self.damage}")

        def calculate_damage(self):
            """Переопределяем расчёт урона для гнома"""
            if random.random() < 0.3:  # 30% шанс критического удара
                damage = self.damage * 2
                print(f"💪 Неожиданная пощёчина ГНОМА! x2 урон!")
                return damage
            else:
                return random.randint(1, self.damage)


    # раса Человек
    class Human(Race):
        def __init__(self, health, damage):
            super().__init__(health, damage)
            self.race_name = 'Человек'

        def describe(self):
            print(f"\nРаса: {self.race_name}")
            print(f"Здоровье: {self.health}/{self.max_health}")
            print(f"Атака: {self.damage}")

        def heal(self):
            """Способность человека лечиться"""
            heal_amount = random.randint(10, 25)
            old_health = self.health
            self.health = min(self.max_health, self.health + heal_amount)
            actual_heal = self.health - old_health
            print(f"💚 Человек лечится! Восстановлено {actual_heal} здоровья")
            print(f"❤️ Текущее здоровье: {self.health}")
            return actual_heal

        def special_attack_effect(self, enemy):
            """Человек может лечиться после атаки"""
            if random.random() < 0.2 and self.is_alive():
                self.heal()


    # ПРОВЕДЕНИЕ ТУРНИРА

    def choose_fighters(all_fighters):
        """Выбор трёх бойцов для турнира с запретом одинаковых рас в первом бою"""

        fighters_pool = all_fighters.copy()

        # Выбираем первого бойца
        fighter1 = random.choice(fighters_pool)
        fighters_pool.remove(fighter1)

        # Выбираем второго бойца
        available_for_fighter2 = []
        for fighter in fighters_pool:
            if fighter.race_name != fighter1.race_name:
                available_for_fighter2.append(fighter)

        if available_for_fighter2:
            fighter2 = random.choice(available_for_fighter2)
        else:
            fighter2 = random.choice(fighters_pool)
            print(f"⚠️ Внимание: все оставшиеся бойцы той же расы, что и {fighter1.race_name}!")

        fighters_pool.remove(fighter2)

        # Третий боец - оставшийся
        fighter3 = fighters_pool[0]

        return fighter1, fighter2, fighter3


    def run_battle(fighter_a, fighter_b, name_a, name_b, is_final=False):
        """Проведение одного боя между двумя бойцами"""

        battle_type = "ФИНАЛЬНЫЙ БОЙ" if is_final else "БОЙ"
        print(f"\n{'=' * 50}")
        print(f"🥊 {battle_type}: {name_a.upper()} vs {name_b.upper()}!")
        print(f"{'=' * 50}")

        round_num = 1
        while fighter_a.is_alive() and fighter_b.is_alive():
            print(f"\n--- РАУНД {round_num} ---")

            # Первый атакует второго
            fighter_a.attack(fighter_b)

            if not fighter_b.is_alive():
                print(f"\n💀 {name_b.upper()} ПОВЕРЖЕН!")
                print(f"🏆 ПОБЕДИТЕЛЬ: {name_a.upper()}!")
                return fighter_a, name_a

            # Второй атакует первого
            fighter_b.attack(fighter_a)

            if not fighter_a.is_alive():
                print(f"\n💀 {name_a.upper()} ПОВЕРЖЕН!")
                print(f"🏆 ПОБЕДИТЕЛЬ: {name_b.upper()}!")
                return fighter_b, name_b

            round_num += 1


    # НАЧАЛО ТУРНИРА

    # Создаём персонажей
    orc = Orc(100, 40)
    dwarf = Dwarf(100, 20)
    human = Human(100, 30)

    all_fighters = [orc, dwarf, human]

    # Выводим характеристики
    print("\n" + "=" * 50)
    print("📋 УЧАСТНИКИ ТУРНИРА:")
    print("=" * 50)
    orc.describe()
    dwarf.describe()
    human.describe()

    # Выбираем бойцов
    fighter1, fighter2, fighter3 = choose_fighters(all_fighters)

    # Сохраняем имена для вывода
    name1 = fighter1.race_name
    name2 = fighter2.race_name
    name3 = fighter3.race_name

    print(f"\n{'=' * 50}")
    print(f"📢 ПЕРВЫЙ БОЙ: {name1.upper()} vs {name2.upper()}")
    print(f"📢 ТРЕТИЙ БОЕЦ ЖДЁТ: {name3.upper()}")
    print(f"{'=' * 50}")

    # Проводим первый бой
    winner, winner_name = run_battle(fighter1, fighter2, name1, name2)

    print(f"\n{'=' * 50}")
    print("✅ ПЕРВЫЙ БОЙ ЗАВЕРШЁН!")
    print(f"{'=' * 50}")

    # Сбрасываем баффы победителя перед финалом (если это Орк)
    if isinstance(winner, Orc):
        winner.reset_for_battle()

    # Проверяем, может ли третий боец участвовать в финале
    if not fighter3.is_alive():
        print(f"\n💀 {name3.upper()} не может участвовать в финале (персонаж мёртв)!")
        print(f"🏆 АБСОЛЮТНЫЙ ПОБЕДИТЕЛЬ ТУРНИРА: {winner_name.upper()}!")
        exit()

    # Показываем состояние перед финалом
    print(f"\n📊 Состояние перед финальным боем:")
    print(f"{winner_name}: ❤️ {winner.health}/{winner.max_health} здоровья | ⚔️ {winner.damage} атаки")
    print(f"{name3}: ❤️ {fighter3.health}/{fighter3.max_health} здоровья | ⚔️ {fighter3.damage} атаки")

    # Проводим финальный бой
    final_winner, final_winner_name = run_battle(winner, fighter3, winner_name, name3, is_final=True)

    print(f"\n{'=' * 50}")
    print("🏆 ТУРНИР ЗАВЕРШЁН!")
    print(f"👑 АБСОЛЮТНЫЙ ПОБЕДИТЕЛЬ: {final_winner_name.upper()}!")
    print(f"{'=' * 50}")

elif menu == 0:
    print('Вы вышли из игры')