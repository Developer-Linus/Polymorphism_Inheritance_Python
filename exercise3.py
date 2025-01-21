class Dog:
    def make_sound(self):
        print("Woof!")
class Cat:
    def make_sound(self):
        print("Meow!")
class Bird:
    def make_sound(self):
        print("Tweet!")
def let_them_speak(obj):
    return obj.make_sound()

dog = Dog()
cat = Cat()
bird = Bird()

let_them_speak(dog)
let_them_speak(cat)  
let_them_speak(bird)  