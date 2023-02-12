class PersistenceManager:
    @staticmethod
    def save_to_file(notepad, file):
        with open(file, mode='w', encoding='utf-8') as f:
            f.write(str(notepad))

    @staticmethod
    def load_from_file(file):
        with open(file, mode='r', encoding='utf-8') as f:
            r = f.read().split('\n')
            res = Notepad(r[0])
            for i in r:
                res.add_note(i)
        return res


class Notepad:
    def __init__(self, name):
        self.name = name
        self.notes = []
        self.count = 0

    def add_note(self, text):
        self.count += 1
        self.notes.append(str(text))

    def __str__(self):
        res = [f'{self.name}:']
        for i, n in enumerate(self.notes):
            res.append(f'{i + 1}: {n}')

        return '\n'.join(res)

    def del_note(self, note_number):
        if note_number <= len(self.notes):
            del self.notes[note_number - 1]
        else:
            raise ValueError('Записи с таким номером не существует')


j = Notepad('Список дел')

j.add_note('Погулять в парке')
j.add_note('Приготовить еду')
j.add_note('Помыть полы в квартире')
j.add_note('Купить новый стул')

print(j)

j.del_note(3)

print(j)

file = 'textfiles/file.txt'

PersistenceManager.save_to_file(j, file)
j2 = PersistenceManager.load_from_file(file)
