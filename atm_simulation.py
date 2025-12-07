import datetime
import os

# --- 1. FILE OPERATIONS ---
def save_data(current_balance, current_pin):
    file = open("bank_data.txt", "w")
    file.write(str(current_balance) + "\n")
    file.write(str(current_pin))
    file.close()

def load_data():
    if os.path.exists("bank_data.txt"):
        file = open("bank_data.txt", "r")
        data = file.readlines()
        file.close()
        
        saved_balance = float(data[0].strip())
        saved_pin = int(data[1].strip())
        return saved_balance, saved_pin
    else:
        return 1500.0, 1234  # Default values

# --- 2. HELPER FUNCTIONS ---
def withdraw(balance, amount):
    if amount > balance:
        print("⚠️ Insufficient funds!")
        return balance
    else:
        return balance - amount

def show_menu():
    print("\n" + "*"*30)
    print("--- ATM SYSTEM ---") 
    print("1 - Check Balance")
    print("2 - Withdraw Money")
    print("3 - Deposit Money")
    print("4 - Transaction History")
    print("5 - Change PIN")
    print("q - Quit")
    print("*"*30)

# --- 3. INITIAL SETUP ---
balance, pin = load_data()
history = []
attempts = 3

# --- 4. SECURITY CHECK ---
print("\n🔒 _______ SECURITY CHECK ________")
while attempts > 0:
    try:
        input_pin = int(input("PLEASE ENTER YOUR 4-DIGIT PIN: "))
    except ValueError:
        print("Please enter numbers only!")
        continue

    if input_pin == pin:
        print("\n✅ LOGIN SUCCESSFUL. WELCOME!")
        break
    else:
        attempts -= 1
        print(f"❌ Incorrect PIN! Remaining attempts: {attempts}")

if attempts == 0:
    print("\n⛔ MAXIMUM ATTEMPTS REACHED. SYSTEM LOCKED.")
    input("Press Enter to exit...")
    exit()

# --- 5. MAIN LOOP ---
while True:
    show_menu()
    choice = input("Select an option: ")

    if choice == "q":
        print("Exiting system... Have a nice day.")
        input("Press Enter to close...")
        break

    elif choice == "1":
        print(f"💰 Current Balance: ${balance}")

    elif choice == "2":
        try:
            amount = float(input("Enter amount to withdraw: "))
            old_balance = balance
            balance = withdraw(balance, amount)
            
            if balance < old_balance:
                print(f"✅ Transaction successful. New Balance: ${balance}")
                time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                history.append(f"{time_now} - Withdrew: ${amount}")
                save_data(balance, pin)
            else:
                print("❌ Transaction failed.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "3":
        try:
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print(f"✅ Transaction successful. New Balance: ${balance}")
            
            time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            history.append(f"{time_now} - Deposited: ${amount}")
            save_data(balance, pin)
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":
        print("\n📜 --- TRANSACTION HISTORY ---")
        for log in history:
            print(log)
        if len(history) == 0:
            print("No transactions yet.")

    elif choice == "5":
        try:
            verify_pin = int(input("Enter current PIN for security: "))
            
            if verify_pin == pin:
                new_pin = int(input("Enter new 4-digit PIN: "))
                pin = new_pin 
                print("✅ PIN successfully changed.")
                print(f"Your new PIN is: {pin}") 
                save_data(balance, pin)
            else:
                print("❌ Incorrect current PIN! Operation cancelled.")    
        except ValueError:
            print("Please enter numbers only.")
   
    else:
        print("⚠️ Invalid selection.")