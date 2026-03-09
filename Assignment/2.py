# QUESTION:
# Create a simple password manager using functions.
# Include login (3 attempts) and track failed attempts.

# Global variables
password = None
failed = []

def add():
    global password
    password = input("enter new password: ")
    print("saved!")

def login():
    if not password:
        print("set password first!")
        return False
    
    for i in range(3, 0, -1):
        p = input(f"enter password ({i} left): ")
        if p == password:
            print("ok!")
            return True
        failed.append(p)
        print("wrong!")
    print("blocked!")
    return False

def edit():
    global password
    if login():
        password = input("enter new: ")
        print("updated!")

def show():
    if login(): print(f"password is: {password}")

def attempts():
    print(f"failed: {failed}")

# Main loop
while True:
    print("\n1.Add 2.Login 3.Edit 4.Show 5.Failed 6.Exit")
    c = input("choice: ")
    if c == '1': add()
    elif c == '2': login()
    elif c == '3': edit() 
    elif c == '4': show()
    elif c == '5': attempts()
    elif c == '6': break
    else: print("invalid!")