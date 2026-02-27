# Simple inheritance

# Base Class
class Animal:
    def __init__(self,name):
        self.__name=name
    def speak(self):
        print(f"Hey {self.__name} make a sound")

# derived class
class Dog(Animal):
    def speak1(self):
        print(f"{self.name} barks")        

animal=Animal("Tommy")  
animal.speak() 
# dog=Dog("Lucy")
# dog.speak()

# Super KeyWord
# Base Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"Hey {self.name} make a sound")


# Derived Class
class Dog(Animal):
    def __init__(self, breed):
        super().__init__("Dog")   # ✅ pass name
        self.breed = breed

    def speak(self):
        super().speak()
        print(f"{self.name} barks. It is a {self.breed}")


dog = Dog("Golden Retriever")
dog.speak()
     