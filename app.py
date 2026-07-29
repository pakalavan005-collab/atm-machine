balance = 5000
pin = 1234

def bal():
    print("Balance amount:", balance)

def deposit():
    global balance
    a = int(input("Enter deposit amount: "))
    balance += a
    print("New balance:", balance)

def withdraw():
    global balance
    b = int(input("Enter withdraw amount: "))
    if balance < b:
        print("Insufficient amount")
    else:
        balance -= b
        print("New balance:", balance)

def change_pin():
    global pin
    old_pin = int(input("Enter current PIN: "))
    if old_pin == pin:
        new_pin = int(input("Enter new PIN: "))
        confirm_pin = int(input("Confirm new PIN: "))
        if new_pin == confirm_pin:
            pin = new_pin
            print("PIN changed successfully.")
        else:
            print("PIN confirmation does not match.")
    else:
        print("Incorrect current PIN.")

user_pin = int(input("Enter your PIN: "))

if user_pin == pin:
    while True:
        print("\nATM Menu")
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Exit")

        c = int(input("Enter your choice: "))

        if c == 1:
            bal()
        elif c == 2:
            deposit()
        elif c == 3:
            withdraw()
        elif c == 4:
            change_pin()
        elif c == 5:
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid option.")
else:
    print("Invalid PIN")
