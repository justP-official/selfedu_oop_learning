class Point:
  "Класс для представления точек на плоскости"
  color = 'red'
  circle = 2


a = Point()

b = Point()

Point.circle = 1

a.color = 'green'

print(a.__dict__)


Point.type_pt = 'disc'

setattr(Point, 'prop', 1) # устанавливает атрибут класса

getattr(Point, 'a', False) # получает атрибут класса

hasattr(Point, 'type_pt') # проверяет, есть ли атрибут класса

delattr(a, 'color') # удаляет атрибут класса

a.x = 1
a.y = 2

b.x = 10
b.y = 20