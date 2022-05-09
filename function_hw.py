#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
def lesser_of_two_evens(num1,num2):
    greater_num = max(num1,num2)
    smaller_num = min(num1,num2)
    if num1 and num2 %2 == 0:
        return smaller_num
    else:
        return greater_num

print(lesser_of_two_evens(2,4))        
print(lesser_of_two_evens(2,5))

#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(word1,word2):
    first_letter1 = word1[0]
    first_letter2 = word2[0]
    return first_letter1 == first_letter2

print(animal_crackers('lala','lala'))
print(animal_crackers('lala','bala'))

#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def makes_twenty(num1,num2):
    check_twenty = 20
    return num1 == check_twenty or num2 == check_twenty or num1 + num2 == check_twenty
        
print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(cap_first_and_fourth):
    out = []
    for index,letter in enumerate(cap_first_and_fourth):
        if index == 0 or index == 3:
            out.append(cap_first_and_fourth[index].upper())
        else:
            out.append(cap_first_and_fourth[index])
    return ''.join(out)

print(old_macdonald('macdonald'))

#MASTER YODA: Given a sentence, return a sentence with the words reversed
def cap_every_other(word):
    return " ".join(word.split()[::-1])
    
result = cap_every_other("We are ready")
print(result)
