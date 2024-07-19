class Account:
    def __init__(self) -> None:
        self.__balance = 0

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, value: float) -> None:
        if value >= 0:
            self.__balance = value

# Usage:
account = Account()

# Using the getter
print(account.balance)  # Output: 0

# Using the setter
account.balance = 100
print(account.balance)  # Output: 100

# Trying to set a negative balance (setter validation will prevent this)
account.balance = -50
print(account.balance)  # Output: 100 (balance remains unchanged)

# Setting a new valid balance
account.balance = 150
print(account.balance)  # Output: 150
 