from abc import ABC, abstractmethod

class Bank(ABC):
    
    def basicinfo(self):
        print("This is a generic bank")
        return "Generic bank: 0"
    
    # any class that inherits from Bank Class must implement withdraw() method
    @abstractmethod
    def withdraw(self):
        pass

class Swiss(Bank):

    def __init__(self) -> None:
        self.__bal = 1000
        
    def basicinfo(self):
        super().basicinfo()
        print("This is the Swiss Bank")
        return f"Swiss Bank: {self.__bal}"
    
    def withdraw(self, amount):
        if amount > self.__bal:
            print("Insufficient funds")
        else:
            self.__bal -= amount
            print(f"Withdrawn amount: {amount}")
            print(f"New Balance: {self.__bal}")
        return self.__bal

# Driver Code
def main():
    assert issubclass(Bank, ABC), "Bank must derive from class ABC"
    s = Swiss()
    print(s.basicinfo())
    s.withdraw(30)
    s.withdraw(1000)

if __name__ == "__main__":
    main()