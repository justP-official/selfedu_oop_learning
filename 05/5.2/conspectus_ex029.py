try:
    # f = open("myfile.txt")
    # f.write("hello")
    with open("myfile.txt") as f:
        f.write("hello")
except FileNotFoundError as z:
    print(z)
except:
    print("Другая ошибка")
else:
    print("Исключений не произошло")
finally:
    print("Блок finally выполняется всегда")
    # if f:
    #     f.close()
    #     print("Файл закрыт")


def get_values():
    try:
        x, y = map(int, input().split())
        return x, y
    except ValueError as z:
        print(z)
        return 0, 0
    finally:
        print("finally выполняется до return")


# x, y = get_values()
# print(x, y)

# try:
#     x, y = map(int, input().split())
#     try:
#         res = x / y
#     except ZeroDivisionError as z:
#         print(z)
# except ValueError as z:
#     print(z)


def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Деление на ноль"


res = 0

try:
    x, y = map(int, input().split())
    res = div(x, y)
except ValueError as z:
    print(z)

print(res)
