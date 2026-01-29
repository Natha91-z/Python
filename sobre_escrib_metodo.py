class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    
    def login(self, username, password):
        if self.username == username and self.password == password:
            return True
        return False


class Admin(User):
    def __init__(self, username, password, email):
        super().__init__(username, password)
        self.email = email
        
    def send_email(self):
        print('>>> envia correo a', self.email)
        
    def login(self, username, password):
        if super().login(username, password):
            self.send_email()


class Organizer(User):
    ...


# Crear instancias
admin = Admin('Admin1', 'password','info@codigofacil.com')
organizer = Organizer('Organizer1', 'password')

# Probar atributos y métodos
print(admin.login('Admin1','password'))          # Admin1
print(organizer.login('Organizer1', 'password'))  # True