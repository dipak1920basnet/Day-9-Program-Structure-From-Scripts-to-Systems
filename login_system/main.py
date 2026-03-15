from database import create_storage, add_data
from auth import read_file, verify_login
def main():
    # Store data
    storage_name = input("Enter the name of the storage:")
    create_storage(storage_name,"name","email","password")
    login_info = input("Enter your name, email, password")
    name, email, password = login_info.split(",")
    add_data(storage_name, name, email, password)
    file = read_file(storage_name)

    verification = verify_login(file, name, email, password)
    if verification == True:
        print("Login is successful")
    else:
        print("Login unsuccessful")
if __name__ == "__main__":
    main()