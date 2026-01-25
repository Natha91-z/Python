# * (posicion) - Tupla
# ** (nombres) -

"""def show_info(username, email, *score,):
    print(username)
    print(email)
    
    average = sum(score) / len(score)
    print(average)
    
    show_info(
        'cody',
        'cody@codigofacilito.com',
        10,10,8,9,7
    )"""
    
def show_info(**user):
    for key, value in user.items():
        print(key, '-', value)
        
show_info(
    username = 'cody',
    email = 'cody@codigogacilito.com',
    password= '123456',
    active = True,  
    courses = ['Python', 'Django', 'Flask'],
)