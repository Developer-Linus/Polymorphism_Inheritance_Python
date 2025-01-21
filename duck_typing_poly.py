class Duck:
    def quack(self):
        return "Duck quacks"
class Person:
    def quack(self):
        return "Person imitates duck"
# Polymorphic behavior using duck typing
def make_sound(obj):
    return obj.quack()
duck = Duck()
person = Person()
print(make_sound(duck))
print(make_sound(person))