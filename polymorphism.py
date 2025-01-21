class Animal:
    def make_sound(self):
        print("Generic animal make sound")
class Dog(Animal):
    def make_sound(self):
        print("Woof!")
animals = [Dog(), Animal()]
for animal in animals:
    animal.make_sound()