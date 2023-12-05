"""
Подвиг 8. Объявите класс CardCheck для проверки корректности информации на пластиковых картах.
Этот класс должен иметь следующие методы:

check_card_number(number) - проверяет строку с номером карты и возвращает булево значение True,
если номер в верном формате и False - в противном случае.
Формат номера следующий: XXXX-XXXX-XXXX-XXXX, где X - любая цифра (от 0 до 9).

check_name(name) - проверяет строку name с именем пользователя карты.
Возвращает булево значение True, если имя записано верно и False - в противном случае.

Формат имени: два слова (имя и фамилия) через пробел, записанные заглавными латинскими символами и цифрами.
Например, SERGEI BALAKIREV.

Предполагается использовать класс CardCheck следующим образом (эти строчки в программе не писать):

is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")
Для проверки допустимых символов в классе должен быть прописан атрибут:

CHARS_FOR_NAME = ascii_lowercase.upper() + digits
Подумайте, как правильнее объявить методы check_card_number и check_name (декораторами @classmethod и @staticmethod).
"""

from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        parts = number.split('-')
        if all(map(lambda x: len(x) == 4, parts)) and len(parts) == 4:
            for item in parts:
                return all(map(lambda x: x.isdigit(), item))
        else:
            return False

    @classmethod
    def check_name(cls, name):
        if len(name.split()) == 2:
            return all(map(lambda x: x in cls.CHARS_FOR_NAME, filter(lambda x: x != ' ', name)))
        return False


print(CardCheck.check_card_number("123q-5678-9012-0000"))
print(CardCheck.check_name("SERGEI BALAKIREV"))
