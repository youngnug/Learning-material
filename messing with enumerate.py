index_count = 0
word = 'abcdefghijklmnop'
for letter in word:
    print(f'At index {index_count} the letter is {letter}')
    if letter == 'g':
        break
    index_count +=1
    

word = 'abcde'
for index, letter in enumerate(word):
    print(f'At the index {index}, the letter is {letter}')
    

word = 'abcdefhijklmnopqrs'
def index(num,letter):
    return (num,letter)


num = [num for num in enumerate(word)]
print(index(num,letter))
