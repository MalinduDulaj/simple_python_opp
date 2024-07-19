class Account:
    def __init__(self) -> None:
        self.__balance =100

    def __str__(self) -> str:
        return f"Account Balance : {self.__balance}"
    
    def get_balance(self) -> float :
        return self.__balance
    

account = Account()
print(account)

#constructors 

class BankAccount:
    def __init__(self,account_number,account_holder,balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

account1 = BankAccount("123456789","Alice",1000.0)


#