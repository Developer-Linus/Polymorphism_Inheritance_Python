class Flyer:
    def fly(self):
        print("flying.......")
class Swimmer:
    def swim(self):
        print("swimming....")
class Duck(Flyer, Swimmer):
    pass

duck = Duck()
duck.fly()
duck.swim()

# In multiple inheritance, child inherits from more than one class. In our case, the child class Duck is inheriting from two parent classes: Flyer and Swimmer.
