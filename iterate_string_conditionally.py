def func(word):
    converted = []
    for i in range(len(word)):
        if i %2 != 0:
            converted.append(word[i].upper())
        else:
            converted.append(word[i].lower())
    return ''.join(converted)
#or

def func(word):
    converted = []
    for i,letter in enumerate(word):
        if i %2 != 0:
            converted.append(word[i].upper())
        else:
            converted.append(word[i].lower())
    return ''.join(converted)
  
#enumerate returns indexed tuples, so --> (0,e), (1,n) etc.
#So if I designate i as the index and letter as the letter in the for statement, enumearte can be used instead of range(len(word))
#Note that range(len(word)) is the same idea as for (i = 0; i < word.length; i++)
print(func('ilovegranite'))
