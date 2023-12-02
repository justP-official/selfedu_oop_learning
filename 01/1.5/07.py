"""
Подвиг 7. Объявите в программе следующие несколько классов:

CPU - класс для описания процессоров;
Memory - класс для описания памяти;
MotherBoard - класс для описания материнских плат.

Обеспечить возможность создания объектов каждого класса командами:

cpu = CPU(наименование, тактовая частота)
mem = Memory(наименование, размер памяти)
mb = MotherBoard(наименование, процессор, память1, память2, ..., памятьN)
Обратите внимание при создании объекта класса MotherBoard можно передавать несколько объектов класса Memory,
максимум N - по числу слотов памяти на материнской плате (N = 4).

Объекты классов должны иметь следующие локальные свойства:

для класса CPU: name - наименование; fr - тактовая частота;

для класса Memory: name - наименование; volume - объем памяти;

для класса MotherBoard:
name - наименование;
cpu - ссылка на объект класса CPU;
total_mem_slots = 4 - общее число слотов памяти (атрибут прописывается с этим значением и не меняется);
mem_slots - список из объектов класса Memory (максимум total_mem_slots = 4 штук по максимальному числу слотов памяти).

Класс MotherBoard должен иметь метод get_config(self) -
для возвращения текущей конфигурации компонентов на материнской плате в виде следующего списка из четырех строк:

['Материнская плата: <наименование>',
'Центральный процессор: <наименование>, <тактовая частота>',
'Слотов памяти: <общее число слотов памяти>',
'Память: <наименование_1> - <объем_1>; <наименование_2> - <объем_2>; ...; <наименование_N> - <объем_N>']

Создайте объект mb класса MotherBoard с одним CPU (объект класса CPU) и двумя слотами памяти (объекты класса Memory).
"""


class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, mem_slots, total_mem_slots=4):
        self.name = name
        self.cpu = cpu
        self.mem_slots = mem_slots[:total_mem_slots]
        self.total_mem_slots = total_mem_slots

    def get_config(self):
        tmp = [f'{item.name} - {item.volume}' for item in self.mem_slots]
        return [f'Материнская плата: {self.name}',
                f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
                f'Слотов памяти: {self.total_mem_slots}',
                f'Память: {"; ".join(tmp)}']


mb = MotherBoard('AMD', CPU('Intel', '2400'), [Memory('Samsung', '8'), Memory('Samsung', '6')])

print(mb.get_config())
