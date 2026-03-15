def read_file(file_name):
    with open(f"{file_name}.csv","r") as file:
        content = file.readlines()
    
    return content

def verify_login(content:list, name, email, password):
    for i in content:
        data = i.strip()
        print(data)
        auth_name, auth_email, auth_password = data.split(",")
        if (name==auth_name, email==auth_email, password==auth_password):
            return True
    return False
    
