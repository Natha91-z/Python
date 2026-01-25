# parametros ej

def count_to(number):
    for i in range(1, number + 1):
        print(i)
   
def multiply(number1, number2):
    result = number1 * number2
    print(f" El resultado de la operacion es: {result}")
    
def full_name(first_name, last_name, prefix):
    full_name = f"{prefix} {first_name} {last_name}"
    print(full_name)
        
count_to(10) # aragumento
multiply(10, 20)
full_name("Juan", 
          "Perez", 
          "Sr.")

