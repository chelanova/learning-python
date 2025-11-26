# Methods: set_pin(), verif_pin(), withdraw(), deposite(), balance(), get_balance()
class SecureBankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance
        self.__pin = None
        
    def set_pin(self, pin):
        if len(str(pin)) == 6:
            self.__pin = pin
            return  "PIN set successfully"
        return "PIN must be 6 digits"
    
    def verif_pin(self, pin):
        return self.__pin == pin
    
    def deposite(self, amount, pin):
        if not self.verif_pin(pin):
            return "PIN invalid"
        if amount > 0:
            self.__balance += amount
            return f"Deposited: +Rp.{amount:,}, New balance Rp.{self.__balance}"
        return "Invalid amount!"
    
    def withdraw(self, amount, pin):
        if not self.verif_pin(pin):
            return "PIN invalid"
        if amount > self.__balance:
            return "Insufficient funds!"
        if amount > 0:
            self.__balance -= amount
            return f"Deposited: -Rp.{amount:,}, New balance Rp.{self.__balance}"
        return "Invalid amount!"
        
    @property
    def balance(self):
        return f"Balance Rp.{self.__balance}"
    
    def get_balance(self, pin):
        if self.verif_pin(pin):
            return f"Balance: Rp.{self.__balance}"
        return "Invalid PIN"
    
acc = SecureBankAccount("Nova", 160000000)
print(acc.set_pin(123456))
print(acc.verif_pin(123456))
print(acc.deposite(300000, 123456))
print(acc.withdraw(5000000, 123456))
print(acc.get_balance(123456))
    
    

        
    
    
    