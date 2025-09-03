class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        # Initialize account attributes
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = initial_balance
    
    def deposit(self, amount):
        # Add amount to balance with validation
    # check if the amount is positive
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive")    
    
    def withdraw(self, amount):
        # Subtract amount from balance if sufficient funds
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
            else:
                raise ValueError("Insufficient funds for withdrawal")
        else:
            raise ValueError("Withdrawal amount must be positive")
    
    def get_balance(self):
        # Return current balance
        return self.balance
    
    def get_account_info(self):
        # Return formatted account information
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder_name}")
        print(f"Current Balance: ${self.balance:.2f}")


# Create account
account = BankAccount(123456, "John Doe", 1000.50)

# Display initial info
print(account.get_account_info())

# Perform deposit
account.deposit(200.00)
print(f"After Deposit: 200.00")
print(f"New Balance: {account.get_balance()}")

# Perform withdrawal
account.withdraw(500.00)
print(f"After Withdrawal: 500.00")
print(f"New Balance: {account.get_balance()}")
