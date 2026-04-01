from abc import ABC, abstractmethod
from datetime import datetime
from typing import List
# using abstract class and methods + polymorphism

class Customer():
    def __init__(self, name = "Account User"):
       self.name = name
       self.accounts: List['BankAccount'] = []  # not List[BankAccount] or [BankAccount] or ['BankAccount']

    def __str__(self):
        return self.name
    
    def addAccount(self, a):
        self.accounts.append(a)
        return a

    def getAccount(self, n):
        if 0 <= n < len(self.accounts):
            return self.accounts[n]
        return None

    def get_total_balance(self):
        total = 0
        for acc in self.accounts:
            total += acc.getBalance()
        print("Total Balance: ", total, " Baht")
    
    # printing user and it's accounts
    def printStatus(self):
        print(self.__str__())
        for a in self.accounts:
            print("", end="     ")
            a.printStatus()

class BankAccount(ABC):
    def __init__(self, bank_name, owner: Customer, balance = 0.0):
        self.bank_name = bank_name
        self.balance = balance
        self.acc_id = None
        self.owner = owner
        self.bankTransactions: List['BankTransaction'] = [] 

    @abstractmethod
    def __str__(self):
        raise NotImplementedError("users must define __str__ to use this base class")
    
    def deposit(self, m: float, person): 
        old_balance = self.balance
        self.balance += m
        self.bankTransactions.append(BankTransaction(m, old_balance, self.balance, datetime.now(), person, "Deposit"))
        

    @abstractmethod
    def withdraw(self, m, person):
        raise NotImplementedError("users must define this to use this base class")

    def transfer(self, m, o: 'BankAccount', person):
        old_balance = self.balance
        self.balance -= m
        o.deposit(m, person)
        self.bankTransactions.append(BankTransaction(m, old_balance, self.balance, datetime.now(), person, f"Transfer to {o.bank_name}"))  # Fixed

    @abstractmethod
    def accountDetail(self):
        raise NotImplementedError("users must define this to use this base class")

    def getBalance(self):
        return self.balance
    
    @abstractmethod
    def printStatus(self):
        raise NotImplementedError("users must define this to use this base class")
    
    def printBankTransaction(self):
        for t in self.bankTransactions:
            t.printDetail()
        

class SavingAccount(BankAccount):
    def __init__(self, bank_name, owner, balance=0.0, ):
        BankAccount.__init__(self, bank_name, owner, balance)
        self.interest = 1.0

    def __str__(self):
        return f"Saving Account ({self.bank_name}) - Owner: {self.owner}"

    def withdraw(self, m, person):
        if self.balance < m:
            print("Insufficient balance! Withdraw not allowed")
            return
        old_balance = self.balance
        self.balance -= m
        self.bankTransactions.append(BankTransaction(m, old_balance, self.balance, datetime.now(), person, "Withdraw"))

    def accountDetail(self):  # Implemented abstract method
        return f"Saving Account - Bank: {self.bank_name}, Balance: {self.balance}, Interest: {self.interest}%, Owner: {self.owner}"

    def printStatus(self):
        print(f"Saving Account of Customer: {self.owner}, Balance: {self.balance}, Interest: {self.interest}%")
        
class OverdrawnAccount(BankAccount):
    def __init__(self, bank_name, owner: Customer, balance=0.0):
        BankAccount.__init__(self, bank_name, owner, balance)
        self.overdrawn_limit = 5000

    def __str__(self): 
        return f"Overdrawn Account ({self.bank_name}) - Owner: {self.owner}"

    def withdraw(self, m, person):
        if self.overdrawn_limit + self.balance < m:
            print("Overdrawn Limit Exceeded! Withdraw Not allowed")
            return
        
        old_balance = self.balance
        self.balance -= m
        self.bankTransactions.append(BankTransaction(m, old_balance, self.balance, datetime.now(), person, "Withdraw"))

    def accountDetail(self):
        return f"Overdrawn Account - Bank: {self.bank_name}, Balance: {self.balance}, Overdrawn Limit: {self.overdrawn_limit}, Owner: {self.owner}"

    def printStatus(self):
        print(f"Overdrawn Account of Customer: {self.owner}, Balance: {self.balance}, Overdrawn Limit: {self.overdrawn_limit}")

class BankTransaction():
    def __init__(self, amount, old_balance, new_balance, timestamp, depositor, ttype):
        self.amount = amount
        self.old_balance = old_balance
        self.new_balance = new_balance
        self.timestamp = timestamp
        self.depositor = depositor
        self.ttype = ttype

    def printDetail(self):
        print(f"Amount: {self.amount}, Depositor: {self.depositor}, Type: {self.ttype}, Old Balance: {self.old_balance}, New Balance: {self.new_balance}, Timestamp: {self.timestamp}")


if __name__ == "__main__":
    
    # Create customers
    customer1 = Customer("John Doe")
    customer2 = Customer("Jane Smith")
    
    print("\n--- Creating Accounts ---")
    # Create accounts
    saving_acc = SavingAccount("SCB Saving",customer1, 10000)
    current_acc = OverdrawnAccount("Kbank Current", customer1, 5000)

    jane_acc = SavingAccount("BBL Saving", customer2.name)
    
    # Add accounts to customers
    customer1.addAccount(saving_acc)
    customer1.addAccount(current_acc)
    customer2.addAccount(jane_acc)
    
    print(f"Created: {saving_acc}")
    print(f"Created: {current_acc}")
    print(f"Created: {jane_acc}")
    
    print("\n--- Initial Status ---")
    customer1.printStatus()
    print()
    customer2.printStatus()
    
    print("\n--- Test Deposit ---")
    saving_acc.deposit(2000, "John Doe")
    print(f"Deposited 2000 to {saving_acc.bank_name}")
    saving_acc.printStatus()
    
    print("\n--- Test Withdraw (Saving Account) ---")
    saving_acc.withdraw(3000, "John Doe")
    print(f"Withdrew 3000 from {saving_acc.bank_name}")
    saving_acc.printStatus()
    
    print("\n--- Test Withdraw (Insufficient Balance) ---")
    saving_acc.withdraw(15000, "John Doe")
    
    print("\n--- Test Withdraw (Current Account with Overdraft) ---")
    current_acc.withdraw(7000, "John Doe")  # Balance 5000 + Limit 5000 = can withdraw up to 10000
    print(f"Withdrew 7000 from {current_acc.bank_name}")
    current_acc.printStatus()
    
    print("\n--- Test Withdraw (Exceed Overdraft Limit) ---")
    current_acc.withdraw(5000, "John Doe")  # Balance -2000 + Limit 5000 = only 3000 left
    
    print("\n--- Test Transfer ---")
    jane_acc.transfer(1500, saving_acc, "Jane Smith")
    print(f"Transferred 1500 from Jane's account to John's saving account")
    customer1.printStatus()
    print()
    customer2.printStatus()
    
    print("\n--- Total Balances ---")
    customer1.get_total_balance()
    customer2.get_total_balance()
    
    print("\n--- Account Details ---")
    print(saving_acc.accountDetail())
    print(current_acc.accountDetail())
    print(jane_acc.accountDetail())
    
    print("\n--- Transaction History (John's Saving Account) ---")
    saving_acc.printBankTransaction()
    
    print("\n--- Transaction History (Jane's Account) ---")
    jane_acc.printBankTransaction()
