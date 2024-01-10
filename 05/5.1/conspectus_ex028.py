try:
    f = open("myfile2.txt")
except FileNotFoundError:
    print("Невозможно открыть файл")

try:
    x, y = map(int, input().split())
    res = x / y
except ValueError:
    print("Ошибка типа данных")
except Exception:
    print("Деление на ноль")

print("Штатное завершение")
