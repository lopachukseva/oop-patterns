class Database:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        Database.__instance = None

    def __init__(self, user, password, port):
        self.user = user
        self.password = password
        self.port = port

    def connect(self):
        print(f'Соединение установлено! Пользователь: {self.user}, порт: {self.port}')


db1 = Database('Vladislav', 'o35w257g3', 8080)
db2 = Database('Sergey', 'yg2s3557f8', 4040)

print(id(db1) == id(db2))
