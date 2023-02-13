class ThreadData:
    __shared_attributes = {
        'name': 'thread',
        'data': {},
    }

    def __init__(self):
        self.__dict__ = self.__shared_attributes


td1 = ThreadData()
td2 = ThreadData()

print(td1.__dict__, td2.__dict__, sep='\n', end='\n-------\n')

td2.name = 'something'

print(td1.__dict__, td2.__dict__, sep='\n', end='\n-------')
