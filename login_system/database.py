def create_storage(file_name, name, email, password):
    with open(f"{file_name}.csv","w") as file:
        file.write(f"{name},{email},{password}\n")

def add_data(file_name, name, email, password):
    with open(f"{file_name}.csv","a") as file:
        structure = name + "," + email + "," + password + "\n"
        file.write(structure)

