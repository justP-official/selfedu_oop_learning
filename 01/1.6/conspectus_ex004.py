class Point:
  def __new__(cls, *args, **kwargs):
    print("вызов __new__ для " + str(cls))
    return super().__new__(cls)

  def __init__(self, x=0, y=0):
    print("вызов __init__ для " + str(self))
    self.x = x
    self.y = y

# pt = Point(1, 2)

# Singleton
class DataBase:
  __instanse = None

  def __new__(cls, *args, **kwargs):
    if cls.__instanse is None:
      cls.__instanse = super().__new__(cls)

    return cls.__instanse
  
  def __del__(self):
    DataBase.__instanse = None

  def __init__(self, user, psw, port):
    self.user = user
    self.psw = psw
    self.port = port

  def connect(self):
    print(f"connection with DB: {self.user}, {self.psw}, {self.port}")

  def close(self):
    print("closing connection with DB")

  def read(self):
    return "Data"
  
  def write(self, data):
    print(f"writing in DB {data}")

db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40)

print(id(db), id(db2))