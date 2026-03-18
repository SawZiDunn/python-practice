class Account:
    def __init__(self):
        self.__balance = 0

    # everytime we call obj.balance, this method will work
    @property
    def balance(self):
        return self.__balance

    def deposit(self, n):
        self.__balance += n

    def withdraw(self, n):
        self.__balance -= n


def main():
    account = Account()
    print("Balance:", account.balance)
    
    account.deposit(1000)
    print("Balance:", account.balance)
    account.withdraw(80)
    print("Balance:", account.balance)
    
    account.balance = 500  # This will raise an error since balance has no setter



    # print("Balance:", account.__balance) # This will raise an error since __balance is private




if __name__ == '__main__':
    main()