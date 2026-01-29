class User:
    def __init__(self, username, password, email=None, rol='Organizer'):
        self.username = username
        self._password = password
        self.email = email
        self.rol = rol
        
    @property
    def password(self):
        if self.rol == 'Admin':
            return self._password
        return None
    
    @password.setter
    def password(self, new_password):
        if self.rol == 'Admin':
            self._password = new_password


# Crear instancia FUERA de la clase
user1 = User(
    username='Codigofacilito',
    password='password123',
    rol='Admin'
)

# Cambiar la contraseña
user1.password = 'Now Password!!'

# Imprimir resultados
print(user1.password)