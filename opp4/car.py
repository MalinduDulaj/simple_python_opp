class Engine:
    def ingine(self):
        print("Engine igniting......")


class Horn:
    def honk(self):
        print("beep beep")


class Car:
    def __init__(self):
        self.engine = Engine()
        self.horn = Horn()

    def start (self):
        self.engine.ingine()

    def honk (self):
        self.horn.honk()


car = Car()
car.start()
car.honk()