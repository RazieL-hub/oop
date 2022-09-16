class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"Connected to DB: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("Close connect")

    def read(self):
        print("Read data from DB")

    def write(self, data: str):
        print(f"Write to DB {data}")


db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40)

print(id(db))
print(id(db2))

print(db2.user)
print(db2.psw)
print(db2.port)

print(db.user)
print(db.psw)
print(db.port)

print(dir(db))
print(dir(db2))