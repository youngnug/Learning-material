mystring = 'hello'

mylist = []
#for loop - makes string 'hello' into a list of each indiviudal letter
for letter in mystring:
    mylist.append(letter)
print(mylist)

#flat for loop does the same things but quicker
mylist = [letter for letter in mystring]
print(mylist)
#for loop -  creates a list from 0-100
mylist = []
for num in range(0,100):
    mylist.append(num)
print(mylist)

#flat for loop - does the same thing but much faster
mylist = [num for num in range(0,100)]
print(mylist)

#This squares the temp variable within a range of 0,11 and then uses mod 2 = 0 to generate a list of all the even numbers.
mylist = [x**2 for x in range(0,11) if x%2==0]
print(mylist)

#These do the same things. These are called flattened for loops. The examples above are a really quick way to generate a large list of numbers
celsius = [0,10,20,30,40]
fahrenheight = []
for temp in celsius:
    fahrenheight.append(9/5*temp+32)
print(fahrenheight)
#Converts celsisus to fahrenheight
fahrenheight = [C for temp in celsius]
print(fahrenheight)

#Idk how I made it work, but this is code converted celsuis to fahrenheight while accepting both intergers and floating point numbers.
def convert(celsius,fahrenheight):
    #Some Fun

def convert(celsius,fahrenheight):
    return int(fahrenheight)
    
celsius = float(input('Type in the temperature in Celsius: '))

fahrenheight = 9/5*celsius+32

print(f'The temperature in Fahrenheight is {fahrenheight}')
