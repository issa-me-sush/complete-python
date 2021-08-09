#comparison operators
print(2.0==2)#T
print('hello'=='Hello')#F
print(2==2)#T
print(3>=5)
print(3<=5)
print(3!=5)
print(5!=5)
print(5>10)
print(5<10)
print('chaining comparison operators - logical operators')
print(1==1 and 'H'=='h')
print(1==1 or 'H'=='h')
print(not(1==1 or 'H'=='h'))
print(1>2<3)#same as 1>2 and 2<3
print(1>2 and 2<3)
#if,else,elif - INDENTATION
language = input('choose language:')
if language == 'spanish':
    print("hola")
elif language == 'english':
    print("hello")
elif language == 'japanese':
    print("moshi moshi")
else:
    print("not a valid language")
#for loop
 
languages =["english","japanese","spanish"]

for lang in languages:
    print(lang)
sumoflist=0
list1 = [8,5,6,7,325,63,42]
for number in list1:
    sumoflist+=number

print(f'sum of the list is {sumoflist}')

for var in 'hai senpai!':
  print(var)

for var in list1:
    print("for loop list traversal")

#tuple unpacking
list2 = [(1,5),(5,6),(7,8)]
for var in list2:
    print(var)     

for a,b in list2:
    print(a)

#for loop with dictionary
dict1 = {'a':90,'b':80,'c':70}

for var in dict1.keys():
    print(var)

for a,b in dict1.items():
    print(b)

for var in dict1.items():
    print(var)
#remember dictionaries are unordered
#while loop
x=0

while x<3:
     print(x)
     x+=1
else:
    print('now x is equal to 3')

#pass - does nothing at all(just a place holder , to prevent errors);break - breaks out of the current closest
#  enclosing loop; continue - goes to the top of the closest enclosing loop

y=0
for x in 'four':
    if y%2==0:
       print(f'{y} is an even number')
    else:
        continue
    y+=1  
y=0   
for x in 'four':
    if y%2==0:
       print(f'{y} is an even number')
    else:
        break
    y+=1 
y=0
for x in 'four':
    if y%2==0:
       print(f'{y} is an even number')
    else:
        pass
    y+=1   
#other useful operators
for  x in range(0,9,2):
    print(x)  
print(list(range(0,6,2)))#generator
y=0
for x in 'word':
    print(f'the letter at index {y} is {x}')
    y+=1

word1 = 'happy'
y=0
for _ in word1:
    print(f'the letter at index {y} is {word1[y]}')
    y+=1
for _ in enumerate(word1):
    print(_)
list2 =['a','b','c','d','e']

for x in zip(list1,list2):#zps or combines lists until the size of the smalles list among them
    print(x)

for a,b in zip(list1,list2):
     print(a)
print(list( zip(list1,list2)))

print('x' in ['x','y','z'])
print('x' in [1,2,3])
print('a' in dict1)
print('a' in dict1.values())
print('a' in dict1.keys())
print(70 in dict1)# looks only into keys, same as using dict1.keys()
print(70 in dict1.keys())
print(70 in dict1.values())
print(max(list1))
print(min(list1))
print(min(list2))
print(max(list2))
print(list1)
from random import shuffle
from random import randint
print(shuffle(list1))#shuffle just shuffles that list, doesnt return anything
print(list1)
print(randint(0,100))#randint returns a random integer

name = input('enter your name:')
print(name)

num   = int(input('enter a number')) #important to type cast . or else it gets saved as a string by default
print(num)


