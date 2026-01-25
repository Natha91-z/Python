def calculate_total(price, tax=0.05, discount=0):
    total = price + (price * tax) - discount
    return total

total = calculate_total(100, 0.07, 5)
print("Total", total)

#asignar un valor de derecha a izquierda 

total = calculate_total(100, 0.07)
print("Total", total)

total = calculate_total(100)
print("Total", total)

total = calculate_total(
    price=100,
    tax=0.07,
    discount=5
    )
print("Total", total)