'''Принцип инверсии зависимостей утверждает, что высокоуровневые классы (или высокоуровневые модули) в коде
не должны напрямую зависеть от низкоуровневых модулей. Вместо этого они должны зависеть от абстракций.
Абстракция - абстрактный класс или класс с абстрактными методами. По сути нужно зависеть от интерфейсов, а не от
конкретных реализаций, потому что таким образом можно поменять один на другой.
'''

from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipsBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass


class Relationships(RelationshipsBrowser):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:
    def __init__(self, browser, name):
        for p in browser.find_all_children_of(name):
            print(f'{name} has a child called {p}')


john = Person('John')
child1 = Person('Chris')
child2 = Person('Mad')

relationships = Relationships()

relationships.add_parent_and_child(john, child1)
relationships.add_parent_and_child(john, child2)

Research(relationships, 'John')
