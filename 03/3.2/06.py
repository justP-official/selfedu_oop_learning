"""
Подвиг 6. Предположим, вам необходимо создать программу по преобразованию списка строк, например:

lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
в следующий фрагмент HTML-разметки (многострочной строки, кавычки выводить не нужно):

'''<ul>
<li>Пункт меню 1</li>
<li>Пункт меню 2</li>
<li>Пункт меню 3</li>
</ul>'''

Для этого необходимо объявить класс RenderList, объекты которого создаются командой:

render = RenderList(type_list)
где type_list - тип списка (принимает значения: "ul" - для списка с тегом <ul> и "ol" - для списка с тегом <ol>).
Если значение параметра type_list другое (не "ul" и не "ol"), то формируется список с тегом <ul>.

Затем, предполагается использовать объект render следующим образом:

html = render(lst) # возвращается многострочная строка с соответствующей HTML-разметкой
Пример использования класса (эти строчки в программе писать не нужно):

lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
P.S. На экран ничего выводить не нужно.
"""


class RenderList:
    def __init__(self, tag):
        self.tag = tag if tag in ('ol', 'ul') else 'ul'

    def __call__(self, lst, *args, **kwargs):
        items = '\n'.join([f"<li>{i}</li>" for i in lst])
        return f"""<{self.tag}>
{items}
</{self.tag}>"""


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)
