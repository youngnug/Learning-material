#Python stuff


mylist = [(1,2),(3,4),(5,6),(7,8)]
print(len(mylist))
for x,y in mylist:
    print(x)
    print(y)
    
    
mylist = [(1,2,3),(4,5,6),(7,8,9,)]
print(len(mylist))
for x,y,z in mylist:
    print(x)
    print(y)
    print(z)
    
d = {'K1':1, 'K2':2, 'K3':3}
for x in d.items():
    print(x)


x = 100
while x < 5:
    print(f'The currrent value of x is {x}')
    x = x + 1 #can write this as x +=1
else:
    print(f'Sorry, {x} is not less than 5!')


bluh = 'sammy'
for x in bluh:
    if x == 'a': 
        break
    print(x)
    
    
x = 0
# this says --> X is equal to 0. While x is less than 5, break if x ever equals 2. You're then printing x +=1 which means the loop is adding to zero each iteration.
#You can put the x += 1 before the print(x) but it will start at 1 instead since you're adding 1 before printing.
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1
