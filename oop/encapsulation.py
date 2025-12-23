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

    print("Balance:", account.__balance)




if __name__ == '__main__':
    main()