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
