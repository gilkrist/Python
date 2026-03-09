# Global variables to store state
stored_password = None
attempts_limit = 3
failed_attempts_list = []

def add_password():
    global stored_password
    stored_password = input("Enter new password to set: ")
    print("Password added successfully!")

def login():
    global failed_attempts_list
    if stored_password is None:
        print("No password set. Please add a password first.")
        return False
    
    attempts = attempts_limit
    while attempts > 0:
        entered_password = input(f"Enter your password ({attempts} attempts left): ")
        if entered_password == stored_password:
            print("Login successful!")
            return True
        else:
            attempts -= 1
            failed_attempts_list.append(entered_password)
            print("Login failed!")
    
    print("Too many attempts. Access denied.")
    return False

def edit_password():
    global stored_password
    if login():
        stored_password = input("Enter new password: ")
        print("Password edited successfully!")

def delete_password():
    global stored_password
    if login():
        stored_password = None
        print("Password deleted successfully!")

def get_password():
    if login():
        print(f"Stored password is: {stored_password}")

def show_attempts():
    print(f"Failed attempts: {failed_attempts_list}")

# ------------------ MENU ------------------
def menu():
    while True:
        print("\nPASSWORD MANAGER")
        print("1. Add Password")
        print("2. Login")
        print("3. Edit Password")
        print("4. Delete Password")
        print("5. Get Password")
        print("6. Show Failed Attempts")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            login()
        elif choice == "3":
            edit_password()
        elif choice == "4":
            delete_password()
        elif choice == "5":
            get_password()
        elif choice == "6":
            show_attempts()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()