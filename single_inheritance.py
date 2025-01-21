class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        print("Generic animal make sound")
# Child class inheriting from one Parent class
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print("Woof!")
dog = Dog("Lassie")
dog.make_sound()

# In single inheritance, the child only inherits behaviours and properties from a single parent class. In this case the class Dog inherits the properties (name) and behaviour (make_sound) from the parent class (Animal).
