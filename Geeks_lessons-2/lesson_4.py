from enum import Enum
from random import randint

class SuperAbility(Enum):
    heal = 1
    critical_damage = 2
    boost = 3
    block_damage_and_revert = 4
class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name
    @property
    def health(self):
        return self.__health
    @health.setter
    def health(self, value):
        self.__health = value
    @property
    def damage(self):
        return self.__damage
    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'

class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence
    def choose_defence(self):
        self.__defence = choice([e for e in SuperAbility])
        self.__defence = choice(abilities_list)
#         print(self.__defence)
    def attack(self, heroes):
        for hero in heroes:
            if type(hero) == Berserk:
                hero.blocked_damage = self.damage // 5

            else:
                hero.health = self.damage

    def __str__(self):
        return (f'BOSS {self.name} HEALTH: {self.health} '
        f'DAMAGE: {self.damage} DEFENCE: {self.__defence}')

class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        if ability == type(SuperAbility):
            self.__ability = ability

    @property
    def ability(self):
        return self.__ability
    def attack(self, boss):
        boss.health -= self.damage
    def apply_super_power(self, boss, heroes):
        pass

class Warrior(Hero):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage, SuperAbility.critical_damage)

    def apply_super_power(self, boss, heroes):
        pass
class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.boost)
    def apply_super_power(self, boss, heroes):
        pass
class Medic(Hero):
    def __init__(self, name, health, damage, health_points):
        super().__init__(name, health, damage, SuperAbility.heal)
        self.__heal_points = health_points
    @property
    def blocked_damage(self):
        return self.__blocked_damage
    def apply_super_power(self, boss, heroes):
        pass
class Berserk(Hero):
    def __init__(self, name, health, damage, health_points):
        super().__init__(name, health, damage, SuperAbility.heal)
        self.__blocked_damage = blocked_damage
    def apply_super_power(self, boss, heroes):
        pass
round_number = 0
def start():
    boss = Boss(name= 'Fiofan', health= 1000, damage= 50)
    warrior_1 = Warrior(name= 'Fiokl', health= 280, damage= 10)
    warrior_2 = Warrior(name= 'Batman', health= 290, damage= 15)
    magic = Magic(name= 'Harry', health= 200, damage= 20)
    doc = Medic(name= 'Hipocrat', health= 150, damage= 5, heal_points= 15)
    assistant = Medic(name= 'Stajer', health= 200, damage= 10, health_points= 5)
    berserk = Berserk(name= 'Viking', health= 210, damage= 10)

    heroes_list = [warrior_1, warrior_2, magic, doc, assistant, berserk]
    show_stats(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)
def show_stats(boss, heroes):
    print(f'ROUND {round_number} --------')
    print(boss)
    for hero in heroes:
        print(hero)
def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence()
    boss.attack(heroes)
    for hero in heroes:
        hero.attack(boss)
        hero.apply_super_power(boss, heroes)
    show_stats(boss, heroes)

def is_game_over(boss, heroes):
    if boss.health <= 0:
        print('Heroes won mfk')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:

start()
# boss = Boss(name: 'Berserk' health:1000, damage:50)
# boss.choose_defence