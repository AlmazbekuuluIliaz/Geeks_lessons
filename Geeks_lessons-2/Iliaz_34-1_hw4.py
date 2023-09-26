from enum import Enum
from random import randint, choice

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
        if value < 0:
            self.__health = 0
        else:
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
        self.__stun = False
    @property
    def stun(self):
        return self.__stun
    @stun.setter
    def stun(self, value):
        self.__stun = value
    @property
    def defence(self):
        return self.__defence
    def choose_defence(self):
        abilities_list = choice([e for e in SuperAbility])
        self.__defence = choice(abilities_list)
#         print(self.__defence)
    def attack(self, heroes):
        for hero in heroes > 0:
            if type(hero) == Berserk and self.__defence != SuperAbility.block_damage_and_revert:
                hero.blocked_damage = self.damage // 5
                hero.health -= self.damage - hero.blocked_damage
            else:
                hero.health = self.damage
    def __str__(self):
        return (f'BOSS {self.name} HEALTH: {self.health} '
                f'DAMAGE: {self.damage} DEFENCE: {self.__defence}'
                f'STUNNRF: {self.__stun}')
class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        if ability == type(SuperAbility):
            self.__ability = ability

    @property
    def ability(self):
        return self.__ability
    def attack(self, boss):
        if self.health > 0 and boss.health > 0:
            boss.health -= self.damage
    def apply_super_power(self, boss, heroes):
        pass

class Warrior(Hero):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage, SuperAbility.critical_damage)

    def apply_super_power(self, boss, heroes):
        coeff = randint(1, 4)
        boss.health -= self.damage * coeff
        print(f'Warrior {self.name} hits critically {self.damage * coeff}')
class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.boost)
    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and boss.health > 0 and type(hero) != Witcher:
                hero.damage += 10
class Medic(Hero):
    def __init__(self, name, health, damage, health_points):
        super().__init__(name, health, damage, SuperAbility.heal)
        self.__heal_points = health_points
    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self != hero and type(hero) != Ghoust:
                hero.health += self.__heal_points
class Berserk(Hero):
    def __init__(self, name, health, damage, health_points):
        super().__init__(name, health, damage, SuperAbility.block_damage_and_revert)
        self.__blocked_damage = 0
    @property
    def blocked_damage(self):
        return self.__blocked_damage
    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value
    def apply_super_power(self, boss, heroes):
        boss.health -= self.__blocked_damage
class Thor(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.critical_damage)

    def apply_super_power(self, boss, heroes):
        super_punch = randint(1, 6)
        if super_punch == 3:
            boss.damage = 0
            boss.stun = True
            print(f'Boss {boss.name} оглушен героем {self.name} на раунд')
        else:
            boss.stun = False
            boss.damage = 60

class Witcher(Hero):
    def __init__(self, name, health, damage, chance):
        super().__init__(name, health, damage, SuperAbility.heal)
        self.__chance = chance

    def apply_super_power(self, boss, heroes):

        revive = randint(1,15)
        choice_hero = [hero for hero in heroes if hero.health <= 0 ]
        if revive <= self.__chance and choice_hero:
            revive_hero = choice(choice_hero)
            revive_hero.health = self.health
            self.health = 0
            print(f'{self.name} оживил товарища {revive_hero.name}, пожертвовав собой')

round_number = 0
def start():
    boss = Boss('Fiofan', 4800, 60)
    warrior_1 = Warrior('Fiokl', 280, 25)
    warrior_2 = Warrior('Batman', 290, 20)
    magic = Magic('Harry', 270, 20)
    doc = Medic('Hipocrat', 230, 10, 20)
    assistant = Medic('Stajer', 250, 15, 10)
    berserk = Berserk('Viking', 350, 20)
    thor = Thor('Thor', 320, 30)
    witcher = Witcher('Rudeus', 250, 0, 10)

    heroes_list = [warrior_1, warrior_2, magic, doc, assistant, berserk, thor, witcher]
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
        if (boss.defence != hero.ability and
                hero.health > 0 and boss.health > 0):
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
        print('Boss won mfk')
        return True
    return False

start()
# boss = Boss(name: 'Berserk' health:1000, damage:50)
# boss.choose_defence