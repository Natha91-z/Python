# clave (llave) : valor
# String, duplas, int, float, booleans, func

user ={
    'name': 'Cody',
    'age': 10,
    'active': True,
    'courses': [
        'Python', 'Django', 'Flask'],
    'settings': {123, True},
    3.14: True
}

print('name' in user) 

user_name = user.get('name', 'Lo siento. valor no existe.')
print(user_name)