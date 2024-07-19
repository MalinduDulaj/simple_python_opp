class Car:
    def __init__(self) -> None:
        self.__speed= 0

    def acccelerate(self):
        self.__speed = self.__speed + 10

    def apply_break(self):
        self.__speed = self.__speed - 5

    def get_speed(self):
        return self.__speed


car = Car()
car.acccelerate()
car.acccelerate()
car.acccelerate()
car.apply_break()
car.apply_break()
print(car.get_speed())
