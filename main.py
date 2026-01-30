import sys

class Bank:
    def __init__(self):
        # Key: account_number, Value: dictionary of user details
        self.accounts = {}

    def create_account(self, name, initial_deposit):
        acc_num = len(self.accounts) + 1001  # Simple incremental ID
        self.accounts[acc_num] = {
            "name": name,
            "balance": initial_deposit
        }
        print(f"\n[Success] Account created for {name}. Your Account Number is: {acc_num}")

    def get_account(self, acc_num):
        return self.accounts.get(acc_num)

    def deposit(self, acc_num, amount):
        if acc_num in self.accounts:
            self.accounts[acc_num]['balance'] += amount
            print(f"Deposited ${amount}. New balance: ${self.accounts[acc_num]['balance']}")
        else:
            print("[Error] Account not found.")

    def withdraw(self, acc_num, amount):
        if acc_num in self.accounts:
            if self.accounts[acc_num]['balance'] >= amount:
                self.accounts[acc_num]['balance'] -= amount
                print(f"Withdrew ${amount}. Remaining balance: ${self.accounts[acc_num]['balance']}")
            else:
                print("[Error] Insufficient funds.")
        else:
            print("[Error] Account not found.")

def main():
    bank = Bank()
    
    while True:
        print("\n--- Simple Bank System ---")
        print("1. Open Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")

        if choice == '1':
            name = input("Enter your name: ")
            amount = float(input("Enter initial deposit: "))
            bank.create_account(name, amount)
        
        elif choice == '2':
            acc_num = int(input("Enter account number: "))
            amount = float(input("Enter deposit amount: "))
            bank.deposit(acc_num, amount)

        elif choice == '3':
            acc_num = int(input("Enter account number: "))
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(acc_num, amount)

        elif choice == '4':
            acc_num = int(input("Enter account number: "))
            user = bank.get_account(acc_num)
            if user:
                print(f"\nAccount Holder: {user['name']}")
                print(f"Current Balance: ${user['balance']}")
            else:
                print("[Error] Account not found.")

        elif choice == '5':
            print("Thank you for using our bank. Goodbye!")
            sys.exit()
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()