new_list = []

for num in range(0,100):
    new_list.append(num)
print(new_list)

i=0
while i < 50:
    print(new_list[i])
    i+=1
    if i == 24:
        break
    
new_list[5] = 'pizzadough'
print(new_list)

for x in new_list:
    if type(x) == str:
        new_list.remove(x)
print(new_list)

new_list[4] = 'squishymuffinz'

def remove_string(any_list):
    for i in any_list:
        if type(i) ==str:
            any_list.remove(i)
remove_string(new_list)
print(new_list)
print('LETS GOOOO')
