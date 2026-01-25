def outer_funcion():
    message = "Hola desde la función externa!"
    
    def inner_funcion():
        nonlocal message
        message = 'Info value'
        
    inner_funcion()
    print(message)
    
outer_funcion()