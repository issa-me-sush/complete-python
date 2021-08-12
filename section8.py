#classes
class Cat():
    species='mammal'#common for all objects
    def __init__(self,breed,name,color,spots):#init works like a constructor function of the class, called when class object is made
 #we take in the arguments and assign them using self.attribut_name, conventionally argument and attribut name are same
         self.b=breed
         self.n=name
         self.c=color
         self.s=spots#expecting a boolean
    def meow(self,num):
         while(num>0):
             print(f"nya~, my name is{self.n} and i belong to the species {self.species} or {Cat.species}")
             #self. is for the value associated with that specific instance, whereas Cat. is for the common class value
             num-=1

    

cat1= Cat(breed='persian',name='neko',color='grey',spots=False)
print(cat1.species)

cat1.species='reptile'
print(cat1.species)
print(cat1.b)
print(cat1.n)
print(cat1.c)
print(cat1.s)
cat1.meow(3)
#notice the output carefully and the function definition

#inheritance
class Animal():
     
     def __init__(self):
          print("Animal created")

     def eat(self):
         print("animal is eating")

class Dog(Animal):
    
    def __init__(self):
         print("Dog created")

    
mydog=  Dog()

mydog.eat()

class Dog(Animal):
    
    def __init__(self):
         print("Dog created")

    def eat(self):
        print("dog is eating")

mydog.eat()

class Dog(Animal):
    
    def __init__(self):
         print("Dog created")

    def eat(self):
        print("dog is eating")

mydog=  Dog()
mydog.eat()

class Dog(Animal):
    
    def __init__(self):
         Animal.__init__(self)
         print("Dog created")

    def eat(self):
        print("dog is eating")
mydog=  Dog()

#polymorphism



class Deer():

    def __init__(self):
        print("deer created")

    def eat(self):
        print("I eat grass")
class Lion():

    def __init__(self):
        print("Lion created")

    def eat(self):
        print("I eat Deer")

deer1 = Deer()
lion1 = Lion()

deer1.eat()
lion1.eat()

def food(animal):
    animal.eat()

food(deer1)
food(lion1)

#raising errors

class Pets():
    
    def __init__(self,name):
       self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must be used to implement it")

pet1 = Pets('pet_name')
#pet1.speak()-?gives error

class Dog(Pets):
   
    def speak(self):
        print(self.name + " says woof!")
class Cat(Pets):

    def speak(self):
        print(self.name + " says meow!")

cat1 = Cat('munchkin')
dog1= Dog('fluffy')

cat1.speak()
dog1.speak()
#note: if an __init__ is not defined for the subclass, then it automatically inherits from the base class
#if defined in the subclass, it over rides the baseclass definition, but it(baseclass __init__) can always be called within it

#special methods

class book:

    def __init__(self,name,author,pages):
      self.name = name 
      self.author = author
      self.pages = pages 
    
    def __str__(self): # to return a string to be printed when an object of this class is printed
      return f"{self.name} by "+ self.author

    def __len__(self):
       return self.pages

    def __del__(self):
        print(f"an object of book class with the name {self.name} has been deleted")

    
book1 = book('python mastery','jose portilla',400)

print(book1)
print(len(book1))
del(book1)
#print(book1) -> gives not defined error, as its been deleted or cleared from memory
#solve exercises