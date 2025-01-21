class Vehicle:
    def move(self):
        print("moving........")
class Car(Vehicle):
    pass
class ElectricCar(Car):
    def charge(self):
        print("Charging..........")

tesla = ElectricCar()
tesla.move()
tesla.charge()
# In multilevel inheritance, the child inherits from parent class, which itself inherits from another parent class.

