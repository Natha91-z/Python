def deposit(balance, amount=0):
    return balance + amount

def handle_operation(callback, *args, **kwargs):
    print("El resultado es:")
    
    result = callback(*args, **kwargs)
    print("El resultado es:", result)
    
    
options = input('Ingresa una opcion (a/b):')
balance = int(input('Ingresa el balance: '))
amount = int(input('Ingresa la cantidad: '))

function = options.get(
    options,
    lambda *args, **kwargs: "Opcion no valida"
    )

handle_operation(
    function, 
    balance, amount
    )
