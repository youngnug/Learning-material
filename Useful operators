#This goes over enumerate, more for loops, zip, from random, and input/return
#the \n are just being used to make it easier to see results within my terminal
mylist = [1,2,3,4,5,6]

for num in range(0,6,2):
    print(num)
    
x = list(range(0,6,2))

print(x)
print('\n')
index_count = 0
word = 'abcdefghijklmnop'
for letter in word:
    print(f'At index {index_count} the letter is {letter}')
    if letter == 'g':
        break
    index_count +=1
print('\n')
    
index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count += 1
print("\n")
# This is all just using for loops to grab an index, increasing incrementally by 1. This is so common that python has an operator for this called enumerate

word = 'abcde'
for index, letter in enumerate(word):
    print(index,letter)
print("\n")
   
#zip will only combine the lists to the highest index for the shortest list
list1  = [1,2,3]
list2 = ['a','b','c']
for x,y in zip(list1,list2):
    print(x,y)
print('\n')
#These are all questions that return booleans
print('x' in [1,2,3])
print('a' in 'a happy world')
print('key1' in {'key1':'lalala'})
d = {'key1':'lalala'}
print('lalala' in d.keys())
print('lalala' in d.values())
print('\n')
#from random library, importing different functions. Shuffle will shuffle a list. Randint will produce a random integer with specified range
from random import shuffle
mylist = [1,2,3,4,5,6,7,8,10]
shuffle(mylist)
print(mylist)
from random import randint
new_number = randint(0,1000)
print(new_number)
print('\n')
result = input('Enter a number here: ')
#inputs from the user will show up as a string, to convert a string to a number
float(result) or int(result)
#could also just do
int(result = input('Enter a number here: '))
