# Transaction System Using Functions
from bank import PASSWORD


balance = 0
transactions = []
password = "Manoj@123"
def check_password():
    attempts = 3
    while attempts > 0:
         user_pass = input("Enter your password: ")

         if user_pass == password:
            print("Login Successful!\n")
            return True
         else:
            attempts -= 1
            print("Wrong password! Attempts left:", attempts)

    print("too many wrong attempts.stopped")
    return False

def deposit():
    global balance
    amt = int(input("Enter Deposit Amount: "))
    if amt > 0:
        balance += amt
        transactions.append("Deposited: " + str(amt))
        print("Amount Deposited Successfully!")
    else:
        print("Invalid Amount!")

def withdraw():
    global balance
    amt = int(input("Enter Withdrawal Amount:  "))
    if amt <= balance:
        balance -= amt
        transactions.append("Withdrawn: " + str(amt))
        print("Amount Withdrawn Successfully!")
    else:
        print("Insufficient Balance!")

def check_balance():
    print("Current Balance:", balance)


def show_transactions():
    print("\nTransaction History:")
    if len(transactions) == 0:
        print("No Transactions Yet")
    else:
        for t in transactions:
            print(t)

def main_menu():
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            deposit()
        elif choice == 2:
            withdraw()
        elif choice == 3:
            check_balance()
        elif choice == 4:
            show_transactions()
        elif choice == 5:
            print("thank you")
            break
        else:
            print("Invalid Choice!")

if check_password():
    main_menu()