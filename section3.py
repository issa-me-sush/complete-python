print('hello')
print(1/2)#by default true division is carried out
#generally lower case variable names
#dynamic typing
a=2
print(a)
print(type(a))
a="dynamic typing"
print(a)
print(type(a))
#strings
b='hello bruh'
print(len(b))
#slicing and indexing , they all return character(s)
print(b[1])
print(b[2:])
print(b[2:7])#first index includes the character at that index,second one doesnt,it prints or returns until that index,but not the character at that index
print(b[::2])#third number indicates the number of characters skipped + 1
print(b[-2])# ... -2 -1 <~from the end , remember it starts with -1 from the end
print(b[-1::-1])#reversing string trick
#immutable strings
str = "name"
'''str[0]='s'#returns error'''
print(str)
str="Same"
print(str)
#concatentaion
x= 'is'+str +'sush'
print(x)
print(x*2)
print('2'+'3')
print(2+3)  
print(x.upper())
print(x.lower())
print(b.split())
'''x=x.lower()#try this out'''
print(x.split('s'))
#print formatting
print(f'i am {x}')
'''print('i am {}'.format(x))#another method'''
#lists-uses [],holds several elements of any data types,also mutable, element wise,ordered sequence
list1=['umm',1,'hello world',8.9]
print(list1)
print(list1[1])
list1[1]=93#acceptable, objects are immutable
print(list1[1])
print(list1[2:4])
type(list1.append('appended'))
print(list1[-1])
print(list1.pop())
'''print(list1.sort())#error as sort can only be used for same data type elements'''
y=['b','g','f','a','z','y']
print(y.sort())
print(y)
print(y.reverse())
print(y)
z=['a','A','c','D']
z.sort()#sorts it based on ascii values
print(z)
nestedlist=[a,5,[2,250.1]]
print(f'length of the nested list is {len(nestedlist)}')
print(nestedlist[2][1])
#dictionaries-uses {},unordered mapping , objects linked to keys,no sorting/slicing/indexing, just accessing elements
#using respective keys
dict1={'item1':'apple','item2':'banana'}
print(dict1['item2'])
nesteddict={'apple':{'type1':'california','type2':'kashmir'},'mango':'alphonso'}
print(nesteddict['apple']['type2'])
#lists in dictionary
dictlist={'arr1':[0,5,6,10],'arr2':[9.6,5.7,7,'hello']}
print(dictlist['arr1'][3])
print(dictlist['arr2'][3])
dictlist['arr1'][3]=50
print(dictlist['arr1'][3])
dictlist['arr3']=[a,b,3,5]
dictlist['str']='hello there'
print(dictlist)
#some functions associated with dictionary
print(dictlist.items())
print(dictlist.keys())
print(dictlist.values())
print(f'the number of elements int he dictionary are:{len(dictlist)}')
''' If you do want the capabilities of a dictionary but you would like ordering as well, check out the ordereddict object'''
#tuples- uses (),similar to lists but immutable-mainly used to maintain data integrity in large programs
#where we dont want the data to change in certain places/scenarios
tup=(6,7.8,9,10,78,'hello',10,'hello')
print(tup[-1])
print(tup[1::2])
print(tup.index(7.8))
print(tup.count(10))
print(tup.count('hello'))
print(len(tup))
print(tup)
'''tup[1]='new value'#returns error'''
#sets- unordered collection of unique elements-thus no indexing or slicing- though the set looks sorted
set1=set()
set1.add('a')
set1.add('2')
set1.add('2')
set1.add('3')
print(set1)
list3=[1,1,2,2,5.6,6.7]
print(set(list3))
print(list3)
print(set('parrot'))
print(set('mississippi'))
#booleans
print(True)
print(1<2)
print(None)
b=None#just a placeholder, for variables that are gonna be used later
print(b)
#files I/O
file1 = open('file.txt')
file1.seek(0)
print(file1.read())
file1.close()
#file I/O without worrying about closing the file
with open('file.txt') as my_file:
   textinfile=my_file.read()#indentation is important
print(textinfile)
#file I/O - any location on pc
testfile=open("C:\\Users\\DELL\\Desktop\\coding\\python\\testfile.txt")#path of the file , along with every "\" being replaced with "\\"
print(testfile.read())
print(testfile.readlines())
testfile.close()
#read-r,write-w,append-a,read/write-r+,w+
testfile2=open('testfile2.txt',mode='r')#default mode
print(testfile2.read())
testfile2=open('testfile2.txt',mode='a')
testfile2.write('\nfourth line of text')#on every run, an append takes place
testfile2=open('testfile2.txt',mode='r')
print(testfile2.read())
#for over writing using write mode
testfile2=open('testfile2.txt',mode='w+')#read and write
testfile2.write('this is a text file\nthe second line of the text file')#for some reason , immediate read/print didnt work, only after mode was set to r, it printed
testfile2=open('testfile2.txt',mode='r')#default mode
print(testfile2.read())
#creating/writing a new file
testfile3=open('testfile3.txt',mode='w')
testfile3.write('testfile3 made directly using write function and mode')
testfile3=open('testfile3.txt',mode='r')
print(testfile3.read())
testfile3.close()
testfile2.close()
#all concepts under section 3 covered - attempt assesment test