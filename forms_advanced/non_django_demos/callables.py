class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self, *args, **kwargs):
        pass


p = Person('John', 11)

print(p.name)
print(p())  # if we are not using __call__ method in our class the class is not callable
