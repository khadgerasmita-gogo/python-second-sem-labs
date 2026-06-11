class BankAccount:
    def __init__(self, owner, balance=0):   # balance defaults to 0
        self.owner = owner
        self.balance = balance              # use the value passed in

# Create accounts
account1 = BankAccount("Rasmita", 500)     # balance set to 500
account2 = BankAccount("Arun")             # balance defaults to 0

# Print balances
print(account1.owner, "Balance:", account1.balance)
print(account2.owner, "Balance:", account2.balance)




