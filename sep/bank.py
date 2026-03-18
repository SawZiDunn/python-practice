from abc import ABC, abstractmethod
from datetime import datetime

class Customer():
    def __init__(self, name = ""):
       self.name = name
       self.accounts = []

    def __str__(self):
        return "Customer Name: " + self.name
    
    def addAccount(self, a):
        self.accounts.append(a)
        return a

    def getAccount(self, n):
        if 0 <= n < len(self.accounts):
            return self.accounts[n]
        return None
    
    def printStatus(self):
        print(self.__str__())
        for a in self.accounts:
            print("", end="     ")
            a.printStatus()


class BankTransaction():
    def __init__(self, amount, old_balance, new_balance, timestamp, ttype):
        self.amount = amount
        self.old_balance = old_balance
        self.new_balance = new_balance
        self.timestamp = timestamp
        self.ttype = ttype

    def printDetail(self):
        print("Amount: ", self.amount, ", Type: ", self.ttype, ", Old Balance: ", self.old_balance, ", New_Balance: ", self.new_balance, "timestamp: ", self.timestamp)

class Account(ABC):
    def __init__(self, balance = 0.0, owner = None):
        self.balance = balance
        self.owner = owner
        self.bankTransactions = []

    @abstractmethod
    def __str__(self):
        raise NotImplementedError("users must define __str__ to se this base class")
    
    def deposit(self, m):
        old_balance = self.balance
        self.balance += m
        self.bankTransactions.append(BankTransaction(m, old_balance, self.balance, datetime.now() ,"Deposit"))
        

    @abstractmethod
    def withdraw(self, m):
        raise NotImplementedError("users must define this to se this base class")

    def transfer(self, m, o):
        old_balance = self.balance
        self.balance -= m
        o.deposit(m)
        self.bankTransactions.append(BankTransaction(m, old_balance, self.balance, datetime.now() ,"Transfer from ", o))

    @abstractmethod
    def transferln(self, m, o):
        raise NotImplementedError("users must define this to se this base class")

    @abstractmethod
    def accountDetail(self):
        raise NotImplementedError("users must define this to se this base class")

    @abstractmethod
    def getBalance(self):
        raise NotImplementedError("users must define this to se this base class")
    
    @abstractmethod
    def printStatus(self):
        raise NotImplementedError("users must define this to se this base class")
    
    def printBankTransaction(self):
        for t in self.bankTransactions:
            t.printDetail()
        

class SavingAccount(Account):
    def __init__(self, balance = 0.0, owner = None):
        Account.__init__(self, balance, owner)
        self.interest = 1.0

    def withdraw(self, m):
        old_balance = self.balance
        self.balance -= m
        self.bankTransactions.append(BankTransaction(m, old_balance, self.balance, datetime.now() ,"Withdraw"))

    def printStatus(self):
        print("Saving Account of Customer: ", self.owner, ", Balance: ", self.balance, "Interest: ", self.interest)
        

class CurrentAccount(Account):
    def __init__(self, balance = 0.0, owner = None):
        Account.__init__(self, balance, owner)
        self.overdrawn_limit = -5000

    def withdraw(self, m):
        if self.balance - m < self.overdrawn_limit:
            print("Withdraw Not allowed")
            return
        
        old_balance = self.balance
        self.balance -= m
        self.bankTransactions.append(BankTransaction(m,  old_balance, self.balance, datetime.now() ,"Withdraw"))

    def printStatus(self):
        print("Current Account of Customer: ", self.owner, ", Balance: ", self.balance, "Limit: ", self.overdrawn_limit)







    


    
