# empty class
# a class is like the blue print , like syntax for something.
class House:
    def area(self,a,b):
        area = a*b
        print(area,self)

    def perimeter(self,c,d):
        perimeter = 2*(c+d)
        print(perimeter)

# adding data as instance variable
    def instance(self):
        self.price = 500000
        self.counrty = 'India'
        print('price',self.price)

# for changing the instance values

    def chn_inst(self,colour,name):
        self.colour = colour
        self.name= name
# instances can be used in classes anywhere as well
    def owner(self):
        print('i am the owner',self.name)
# for calling a fuction in the class
        self.instance()

# object is like a house with the same structure
# i just defined some functions in a class which
# implies that I have defined multiple functions which
# fall in the same group.
# now we allot link to that set by using a
# reference , which is an object.
# Then we can access all the functions in that set using that reference ( object)
p1 = House()
p1.area(3,5)
# describing data at an instance
p1.name = 'Hell'
print(p1.name)

# while using data/variables at instance we need to define the function first ith the object
# and then we can call the instance of that class
p2 = House()
p2.instance()
print(p2.price)

# changing the instance for one object doesn't changes it for other
p1.instance()
p1.price = '1000000'
print(p1.price)

print(p2.price)
p1.chn_inst('red','ASh')
print(p1.colour)
p1.owner()






