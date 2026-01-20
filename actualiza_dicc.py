user ={
    'name': 'Cody',
    'age': 10,
    'active': True,
    'courses': [
        'Python', 'Django', 'Flask'],
    'settings': {123, True},
}

#user ['name'] ='Codigo' # actuliza el valor de la llave
#user ['last_name'] = 'Facilito' # agrega una nueva llave con su valor

# otra furma de anadir o actualizar es con update
user.update({
    'name': 'Codigo',
    'last_name': 'Facilito'
})

# setdefault permite agregar una nueva llave al diccionario
user.setdefault('id', 100)

courses = user.get('courses', [])
courses.append('Ruby on Rails')
courses.append('Rust')

user.update({
    'name' : 'Codigo',
    'settings': None,
    'last_name': 'Facilito',
    'courses': courses
})

# para eliminar llaves del
# pop llama por llave y retorna su valor

del user['courses']
value = user.pop('settings')
print(value)

# para limpiar el diccionario clear

user.clear()

print( len(user))
print(user)
