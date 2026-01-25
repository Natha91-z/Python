def deposit(balance, amount=0):
    return balance + amount

def withdraw(balance, amount=0):
    if amount > balance:
        return None
    
    return balance - amount

def default(*args, **kwargs):
    print('opcion no valida')
    
opcions = {
    'a': deposit,
    'b': withdraw
}

option = input('Ingresa una opcion (a/b):')
balance = int(input('Ingresa tu valance'))
amount = int(input('Ingresa la cantidad:'))

function = opcions.get(option, default)
total = function(balance, amount)
print(total)


""" 
Funciones landa
lanbda <parametros>: <body> # siempre retornan un valor 
"""

