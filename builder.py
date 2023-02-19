class HTMLElement:
    ident_size = 2

    def __init__(self, name='', text=''):
        self.name = name
        self.text = text
        self.elements = []

    def __str(self, ident):
        lines = []

        i = ' ' * self.ident_size * ident
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i2 = ' ' * self.ident_size * (ident + 1)
            lines.append(f'{i2}{self.text}')

        for element in self.elements:
            lines.append(element.__str(ident + 1))

        lines.append(f'{i}</{self.name}>')

        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)


class HTMLBuilder:
    def __init__(self, parent_name):
        self.parent = HTMLElement(parent_name)

    def add_child(self, child_name, child_text):
        self.parent.elements.append(HTMLElement(child_name, child_text))

    def __str__(self):
        return str(self.parent)


b = HTMLBuilder('ul')

b.add_child('li', 'Первый элемент')
b.add_child('li', 'Второй элемент')
b.add_child('li', 'Третий элемент')

print(b)
