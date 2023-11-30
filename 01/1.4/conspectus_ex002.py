class Point:
  "Класс для представления точек на плоскости"
  color = 'red'
  circle = 2

  def set_coords(self, x, y):
    # print("вызов метода set_coords " + str(self))
    self.x = x
    self.y = y

  def get_coords(self):
    return (self.x, self.y)


pt = Point()

pt.set_coords(1, 2)

print(pt.get_coords())

# print(pt.__dict__)

pt2 = Point()

pt2.set_coords(10, 20)

# print(pt2.__dict__)

print(pt2.get_coords())