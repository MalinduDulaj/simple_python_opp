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