'''
Подвиг 8. С помощью модуля abc можно определять не только абстрактные методы, но и абстрактные объекты-свойства
(property). Делается это следующим образом:

from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def go(self):
        """Метод для перемещения транспортного средства"""

    @property
    @abstractmethod
    def speed(self):
        """Абстрактный объект-свойство"""
Используя эту информацию и информацию о модуле abc из подвига 6, объявите базовый класс с именем CountryInterface со
следующими абстрактными методами и свойствами:

name - абстрактное свойство (property), название страны (строка);
population - абстрактное свойство (property), численность населения (целое положительное число);
square - абстрактное свойство (property), площадь страны (положительное число);

get_info() - абстрактный метод для получения сводной информации о стране.

На основе класса CountryInterface объявите дочерний класс Country, объекты которого создаются командой:

country = Country(name, population, square)
В самом классе Country должны быть переопределены следующие свойства и методы базового класса:

name - свойство (property) для считывания названия страны (строка);
population - свойство (property) для записи и считывания численности населения (целое положительное число);
square - свойство (property) для записи и считывания площади страны (положительное число);

get_info() - метод для получения сводной информации о стране в виде строки:

"<название>: <площадь>, <численность населения>"

Пример использования классов (эти строчки в программе писать не нужно):

country = Country("Россия", 140000000, 324005489.55)
name = country.name
pop = country.population
country.population = 150000000
country.square = 354005483.0
print(country.get_info()) # Россия: 354005483.0, 150000000
P.S. В программе требуется объявить только классы. На экран выводить ничего не нужно.
'''

from abc import ABC, abstractmethod
# здесь объявляйте классы


class CountryInterface(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def population(self):
        pass

    @population.setter
    def population(self, value):
        pass

    @property
    @abstractmethod
    def square(self):
        pass

    @square.setter
    def square(self, value):
        pass

    @abstractmethod
    def get_info(self):
        pass


class Country(CountryInterface):
    def __init__(self, name, population, square):
        self.__name = name
        self.population = population
        self.square = square

    @property
    def name(self):
        return self.__name

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, value):
        self.__population = value

    @property
    def square(self):
        return self.__square

    @square.setter
    def square(self, value):
        self.__square = value

    def get_info(self):
        return f"{self.name}: {self.square}, {self.population}"


country = Country("Россия", 140000000, 324005489.55)
name = country.name
pop = country.population
country.population = 150000000
country.square = 354005483.0
print(country.get_info().strip())
