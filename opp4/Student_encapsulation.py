class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age #Private attribute

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age > 0:
            self.__age = age
      

student1 = Student("Saman", 14)
student1.set_age(18)
student1.set_age(-235678945)
print(student1.get_age())