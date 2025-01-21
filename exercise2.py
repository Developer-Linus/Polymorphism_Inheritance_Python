class Bird:
    def fly(self):
        print("Flying")
class Mammal:
    def run(self):
        print("Running")
class Bat(Bird, Mammal):
    pass
bat = Bat()
bat.fly()
bat.run()