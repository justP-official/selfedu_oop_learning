"""
Подвиг 10 (на повторение). Объявите класс EmailValidator для проверки корректности email-адреса. Необходимо запретить создание объектов этого класса: при создании экземпляров должно возвращаться значение None, например:

em = EmailValidator() # None
В самом классе реализовать следующие методы класса (@classmethod):

get_random_email(cls) - для генерации случайного email-адреса по формату:
xxxxxxx...xxx@gmail.com, где x - любой допустимый символ в email (латинский буквы, цифры, символ подчеркивания и точка);
check_email(cls, email) - возвращает True, если email записан верно и False - в противном случае.

Корректность строки email определяется по следующим критериям:

- допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и собачка @ (одна);
- длина email до символа @ не должна превышать 100 (сто включительно);
- длина email после символа @ не должна быть больше 50 (включительно);
- после символа @ обязательно должна идти хотя бы одна точка;
- не должно быть двух точек подряд.

Также в классе нужно реализовать приватный статический метод класса:

is_email_str(email) - для проверки типа переменной email, если строка, то возвращается значение True, иначе - False.

Метод is_email_str() следует использовать в методе check_email() перед проверкой корректности email.
Если параметр email не является строкой, то check_email() возвращает False.

Пример использования класса EmailValidator (эти строчки в программе писать не нужно):

res = EmailValidator.check_email("sc_lib@list.ru") # True
res = EmailValidator.check_email("sc_lib@list_ru") # False
P.S. В программе требуется объявить только класс. На экран ничего выводить не нужно.
"""

from string import ascii_lowercase, digits
import random


class EmailValidator:
    CHARS = ascii_lowercase + digits + "@_."

    def __new__(cls, *args, **kwargs):
        return None

    @staticmethod
    def __is_email_str(email):
        return isinstance(email, str)

    @classmethod
    def get_random_email(cls):
        res = ''
        flags = (1, 0)
        for i in range(1, random.randint(2, 153)):
            f = random.choice(flags)
            if f:
                res += random.choice(cls.CHARS)
            else:
                continue
        return res

    @classmethod
    def check_email(cls, email):
        if cls.__is_email_str(email):
            if email.count('@') == 1:
                part_one, part_two = email.split("@")
                if len(part_one) <= 100 and len(part_two) <= 50:
                    if '..' not in email and part_two.count('.') >= 1:
                        return all(map(lambda x: x in cls.CHARS, email))
                return False
            return False
        return False


print(EmailValidator.get_random_email())

res = EmailValidator.check_email("sc_lib@list.ru") # True
print(res)
res = EmailValidator.check_email("sc_lib@list_ru") # False
print(res)
