# print("lorem")
# print("lorem")
# print("lorem")
# e = ZeroDivisionError("Zero division")
# raise e
# print("lorem")
# print("lorem")
# print("lorem")
# print("lorem")


class ExceptionPrint(Exception):
    """Общий класс исключения принтера"""


class ExceptionPrintSendData(ExceptionPrint):
    """Класс исключения при отправке данных принтеру"""
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"Error: {self.message}"


class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f"printing: {str(data)}")

    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExceptionPrintSendData("Printer doesn't respond")

    def send_to_print(self, data):
        return False


p = PrintData()
p.print("123")
# try:
#     p.print('123')
# except ExceptionPrintSendData:
#     print("Printer doesn't respond")
# except ExceptionPrint:
#     print("General printing error")
