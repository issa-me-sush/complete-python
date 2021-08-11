#def keyword
def hello(name):
    print("hello " + name)

hello('hooman')

def add(num1,num2):
   return num1+num2

sum = add(10,20)
print(sum)
sum = add('10','20')
print(sum)


def even_check(num):
   if num%2==0:
       print('its an even number')
   else :
      print('its not an even number')

num = int(input('enter a number:'))
even_check(num)

def evenlistgen(list1):
    evenlist=[]
    for num in list1:
        if num%2==0:
            evenlist.append(num)
    return evenlist


print(evenlistgen([2,4,6,78,90,31]))

#tuple unpacking

def maxcost(list3):
    max = 0
    maxitem=''
    for a,b in list3:
        if b>max:
            max = b
            maxitem = a
        else:
            pass
    return (maxitem,max)

list3 = [('apple',200),('mango',190),('kiwi',300)]

print(maxcost(list3))

a,b = maxcost(list3)
print(a)
print(b)
#interactions between functions
#just using returned value/data from one function as an argument for another function
#*arg and **kwarg
def func1(*args):
    print(args)
tup2 = (5,'a',502,67,'g')
func1(tup2)
func1(5,'a',502,67,'g')
def func2(**kwargs):
    print(kwargs)

dict1= {'apple':'red','mango':'orange','kiwi':'brown'}
func2(apple = 'red',mango='orange',kiwi='brown')
#func2(dict1) give error as dictionary cant be passed as it is, as nested dictionary requires key and value
func2(dictionary1=dict1)
def func3(*x,**y):#the order in which the arguments taken is crucial, also any term can be used instead of args or kwargs
    print(x)
    print(y)

func3(20,4,5,green = 'pears',yellow = 'banana')
#func3(20,4,5,green = 'pears',yellow = 'banana',40) would give error, as the order must be adhered to

#maps
def square(num):
    return num**2
list1=[4,5,6,1,34,23]
print(list(map(square,list1)))
print(list(filter(square,list1)))
for num in map(square,list1):
    print(num)

#filter - filters the elements of a list that return true in the function
def even(num):
    return num%2==0

print(list(filter(even,list1)))
print(list(map(even,list1)))

#lambda expression
cubelambda=lambda num : num*num*num

print(list(map(cubelambda,list1)))
print(list(map(lambda num : num*num*num,list1)))

print(list(filter(lambda num:num%2==0,list1)))
#nested loops - LEGB rule - same as c++, local first, then enclosed loop variable, then global, then built in
print(help(len))#built in function help
z=10
def test(z):
   z=20
   print(z)

test(z)
print(z)

def test2():
   global z
   z=20
   print(z)

test2()
print(z)
#generally returning is preferred over this
w= 8
def test3(z):
 print(w+z)

test3(z)
#solve all exercises