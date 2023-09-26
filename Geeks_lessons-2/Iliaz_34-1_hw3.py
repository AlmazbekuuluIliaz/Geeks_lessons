class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, new_cpu):
        self.__cpu = new_cpu

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, new_memory):
        self.__memory = new_memory

    def make_computations(self):
        return self.__cpu + self.__memory

    def __str__(self):
        return f"Computer [CPU: {self.__cpu}, Memory: {self.__memory}]"

class Phone:
    def __init__(self):
        self.__sim_cards_list = []

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, sim_cards):
        self.__sim_cards_list = sim_cards

    def call(self, sim_card_number, call_to_number):
        if 1 <= sim_card_number <= len(self.__sim_cards_list):
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {self.__sim_cards_list[sim_card_number-1]}")
        else:
            print(f"Сим-карта с номером {sim_card_number} не существует")

    def __str__(self):
        return f"Phone [Sim Cards: {', '.join(self.__sim_cards_list)}]"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self)
        self.sim_cards_list = sim_cards_list

    def use_gps(self, location):
        print(f"Прокладывается маршрут до локации: {location}")

    def __str__(self):
        return f"SmartPhone [CPU: {self.cpu}, Memory: {self.memory}, Sim Cards: {', '.join(self.sim_cards_list)}]"

    def __eq__(self, other):
        return self.memory == other.memory

    def __ne__(self, other):
        return self.memory != other.memory

    def __lt__(self, other):
        return self.memory < other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __gt__(self, other):
        return self.memory > other.memory

    def __ge__(self, other):
        return self.memory >= other.memory


# объекты
computer = Computer("Intel", 8)
phone = Phone()
phone.sim_cards_list = ["Beeline", "Megafon", "MTS"]

smartphone1 = SmartPhone("Snapdragon", 6, ["Beeline", "Megafon"])
smartphone2 = SmartPhone("Exynos", 4, ["MTS", "Tele2"])

# вывод информаций
print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

# Тестировка методов
print(computer.make_computations())
phone.call(1, "+996 777 99 88 11")
smartphone1.use_gps("Дом")
print(smartphone1 == smartphone2)
print(smartphone1 < smartphone2)
print(smartphone1 > smartphone2)
