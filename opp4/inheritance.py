class Animal:
    def speak(self):
        return "Grrr"
    

class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!!"
    
class Lion(Animal):
    def attack(self):
        return "Attacking..."
    

cat = Cat()
print(cat.speak())

dog = Dog()
print(dog.speak())

lion = Lion()
print(lion.speak())
print(lion.attack()) 
    