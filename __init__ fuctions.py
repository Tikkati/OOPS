# at times in a class we have to call the function with instances first everytime
# for avoiding that we use__init__

class User:
    def name(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def display(self):
        print(f'hey {self.name} !! you see {self.age} is just a number for you beacuse what a charming {self.sex} you are ')

person = User()
person.name('Adam', 30, 'male')
person.display()

# excpet that we can use the__init__

class Name:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def display(self):
        print(f'hey {self.name} !! you see {self.age} is just a number for you beacuse what a charming {self.sex} you are ')

person2 = Name('Akshay', 30 ,'Male')
# by using the __init__ we can give values to the
# instances without using the function again and again

person2.display()

