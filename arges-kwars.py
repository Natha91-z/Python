def show_info(username, last_name, *args, active=True, is_super_admin=False, **kwargs):
    print(f"Username: {username}")
    print(f"Last Name: {last_name}")
   
    print(">>> Extra info: ")
    for value in args:
        print(value)
        
    print("active", active)
    print("super admin", is_super_admin)
    
    print(kwargs)
    
show_info(
    'Cody', 'Facilito',
    'info@codigofacilito.com','password123',
    courses=['python','Flask'], is_deleted=False
)
   