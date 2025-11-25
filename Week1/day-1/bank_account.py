#exercise
# TODO: Create a Bank Account class
# Properties: acount_holder, balance,(list)transaction
# Methods: deposit(), withdraw(), get_balance(),get_transaction
from datetime import datetime
waktu = datetime.now()
class BankAccount:
    def __init__(self, account_holder, account_number, balance = 0):
        self.account_holder = account_holder
        self.balance = balance
        self.account_number = account_number
        self.transaction = []
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction.append(f"{waktu} - Deposit: +Rp.{amount:,}")
            return f"Deposited: +Rp.{amount:,}, New balance {self.balance}"
        return "invalid amount"
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        if amount > 0:
            self.balance -= amount
            self.transaction.append(f"{waktu} - Withdrawal: -Rp.{amount:,}")
            return f"Withdrew: -Rp.{amount:,}, New balance {self.balance}"
        return "invalid amount"
    
    def transfer(self, amount, other_account):
        if amount > self.balance:
            return "Insufficient funds!"
        if other_account == self.account_holder:
            return "Transfer invalid!"
        if amount > 0:
            self.balance -= amount
            self.transaction.append(f"{waktu} - Transfer out: Rp.{amount:,} to {other_account.account_number}")
            other_account.balance += amount
            other_account.transaction.append(f"{waktu} - Transfer in: Rp.{amount:,} from {self.account_number}")
            return f"Transfer Rp.{amount:,} to {other_account} succesfull!. New balance: Rp.{self.balance}"
    
    def get_balance(self):
        return f"Current balance: Rp.{self.balance}"
    
    def get_transaction(self):
        print(f"\n=== Transaction History for {self.account_holder} ===")
        for transaction in self.transaction:
            print(transaction)
        print(f"Current balance: Rp.{self.balance}")
        
account1 = BankAccount("anonim",234, 100000)
account2 = BankAccount("nova", 432, 300000)
print(account1.deposit(5000))
print(account1.withdraw(30000))
print(account1.transfer(5000, account2))
account1.get_transaction()
account2.get_transaction()
