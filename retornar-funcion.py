def factory_function(operation):
    def deposit(balance, amount=0):
        return balance + amount
    
    def withdraw(balance, amount=0):
        if amount > balance:
            return None
        
        return balance - amount
    
    default = lanbda *args, **kwargs: 'Opcion no valida'
        
    if option == "deposit":
        return deposit(balance, amount)
    elif option == "withdraw":
        return withdraw
    else:
        return default
    
    opcion = input("Ingrese la operacion  (deposit/withdraw): ")
    func = factory_function(opcion)
    
    print(func(100, 20))
    print(type(func))