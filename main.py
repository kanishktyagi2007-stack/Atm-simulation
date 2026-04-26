# ATM Simulation System

# Initial balance
balance = 1000

# List to store transaction history
transactions = []

# Infinite loop for menu-driven system
while True:
    print("\n====== ATM MENU ======")
    print("1. Display Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Transaction Statement")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    # Display Balance
    if choice == '1':
        print(f"Your current balance is: ₹{balance}")

    # Withdraw Money
    elif choice == '2':
        amount = float(input("Enter amount to withdraw: ₹"))
        
        if amount <= 0:
            print("Invalid amount!")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print(f"Withdrawal successful! New balance: ₹{balance}")
            transactions.append(f"Withdrawn: ₹{amount}")

    # Deposit Money
    elif choice == '3':
        amount = float(input("Enter amount to deposit: ₹"))
        
        if amount <= 0:
            print("Invalid amount!")
        else:
            balance += amount
            print(f"Deposit successful! New balance: ₹{balance}")
            transactions.append(f"Deposited: ₹{amount}")

    # Transaction Statement
    elif choice == '4':
        print("\n====== TRANSACTION STATEMENT ======")
        if not transactions:
            print("No transactions yet.")
        else:
            for i, t in enumerate(transactions, start=1):
                print(f"{i}. {t}")

    # Exit
    elif choice == '5':
        print("Thank you for using ATM. Goodbye!")
        break

    # Invalid Choice
    else:
        print("Invalid choice! Please select from 1 to 5.")