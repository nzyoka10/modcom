# Create an ATM program

# user_lof function - to handle user login
def login(user_pin, max_attempts):
    attempts = 0
    while attempts < max_attempts:
        entered_pin = input("\n Enter your PIN: ")
        if entered_pin == user_pin:
            print("|------------------------------------|")
            print("| _____ Welcome to your ATM. ____   |")
            print("|____________________________________|")
            return True
        else:
            attempts += 1
            print(f"Incorrect PIN. You have {max_attempts - attempts} attempts left.")
    print("Too many incorrect attempts. Your account is blocked.")
    return False

# deposit money function - to handle deposit transactions
def deposit(balance):
    deposit_amount = float(input("Enter amount to deposit: "))
    balance += deposit_amount
    print(f"Deposit of Kes.{deposit_amount:,.2f} successful.")
    print(f"Current balance: Kes.{balance:,.2f}")
    return balance

# withdraw money function - to handle withdrawal transactions
def withdraw(balance):
    withdraw_amount = float(input("Enter amount to withdraw: "))
    
    if withdraw_amount > balance:
        print("Insufficient funds.")
        print(f"Your current balance is: Kes.{balance:,.2f}")
    else:
        remaining_balance = balance - withdraw_amount
        print(f"Withdrawal of Kes.{withdraw_amount:,.2f} successfully completed.")
        print(f"Current balance: Kes.{remaining_balance:,.2f}")
        return remaining_balance
    return balance

# check balance function - to fetch and display users account balance
def total_balance(balance):
    total_balance = balance
    print(f"Account balance: Kes.{total_balance:,.2f}")
    return balance

# Main - program ATM function
def atm_program():
    # Variables
    user_pin = "1234"
    balance = 10000.00
    max_attempts = 3

    # User login
    if not login(user_pin, max_attempts):
        return

    # loop for ATM Menu options
    while True:
        print("\nSelect an option:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            balance = deposit(balance)
        elif choice == '2':
            balance = withdraw(balance)
        elif choice == '3':
            balance = total_balance(balance)
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")

# Call the function to start the program
atm_program()
