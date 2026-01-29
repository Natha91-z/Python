class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self, username, password):
        if self.username == username and self.password == password:
            return True
        return False


class Admin(User):
    ...


class Organizer(User):
    ...


# Crear instancias
admin = Admin('Admin1', 'password')
organizer = Organizer('Organizer1', 'password')

# Probar atributos y métodos
print(admin.username)          # Admin1
print(admin.password)          # password
print(organizer.login('Organizer1', 'password'))  # True