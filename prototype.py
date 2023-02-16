import copy


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'Name: {self.name}, address: {self.address}'


class Address:
    def __init__(self, house, street, city, country):
        self.house = house
        self.street = street
        self.city = city
        self.country = country

    def __str__(self):
        return f'{self.house} {self.street}, {self.city}, {self.country}'


Brandon = Person('Brandon', Address('432', 'Wieden Street', 'Vienna', 'Austria'))
Mike = Person('Mike', Address('19', 'Park Ave Street', 'New York', 'USA'))

Gregory = Mike
Gregory.name = 'Gregory'

print(Brandon, Mike, Gregory, sep='\n')

print(id(Gregory) == id(Mike))

Mike.name = 'Mike'

Gregory = copy.deepcopy(Mike)
Gregory.name = 'Gregory'

print(Brandon, Mike, Gregory, sep='\n')
