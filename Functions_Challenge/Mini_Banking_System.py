CORRECT_PIN = 1234

def check_balance(balance):
    return balance

def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient Balance!")
        return balance
    return balance - amount


attempts = 3

while attempts > 0:
    pin = int(input("Enter your PIN: "))

    if pin == CORRECT_PIN:
        print("✅ Login Successful!")

        balance = float(input("Enter your current balance: "))

        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print(f"Current Balance: ₹{check_balance(balance)}")

        elif choice == 2:
            amount = float(input("Enter amount to deposit: "))
            balance = deposit(balance, amount)
            print(f"Updated Balance: ₹{balance}")

        elif choice == 3:
            amount = float(input("Enter amount to withdraw: "))
            balance = withdraw(balance, amount)
            print(f"Remaining Balance: ₹{balance}")

        else:
            print("Invalid Choice!")

        break

    else:
        attempts -= 1

        if attempts > 0:
            print(f"Incorrect PIN! Attempts left: {attempts}")
        else:
            print("🔒 Account Locked!")