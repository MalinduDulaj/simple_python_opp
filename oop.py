class Account:
    def __init__(self) -> None:
        self.__balance = 0

    def get_balanc(self) -> float :
        return self.__balance
    
    
account = Account()
account.__balance = 1000.0
print(account.get_balanc())
print(account.__balance)
    