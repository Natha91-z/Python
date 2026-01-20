# Metodos: keys, values, items

user ={
    'name': 'Cody',
    'age': 10,
    'active': True,
    'courses': [
        'Python', 'Django', 'Flask'],
    'settings': {123, True},
}

print(
    tuple(user.keys())
)

print(
    list(user.values())
)

print(
    list(user.items())
)