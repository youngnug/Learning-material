#WARMUPS:
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

#LEVEL 1 PROBLEMS
# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(cap_first_and_fourth):
    out = []
    for index,letter in enumerate(cap_first_and_fourth):
        if index == 0 or index == 3:
            out.append(cap_first_and_fourth[index].upper())
        else:
            out.append(cap_first_and_fourth[index])
    return ''.join(out)

#could also do

def old_macdonald(name):
    first_half = name[:3]
    last_half = name[3:]
    return first_half.capitalize() + last_half.capitalize()

print(old_macdonald("macdonald"))
print(old_macdonald('macdonald'))

#MASTER YODA: Given a sentence, return a sentence with the words reversed
def yoda(word):
    return " ".join(word.split()[::-1])
    
result = yoda("We are ready")
print(result)

#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(num):
    #if num is 10 greater than or 10 less than 100, return True. Do the same for 200
    return 90 <= num <= 110 or 190 <= num <= 210
#or 

def almost_there(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

#LEVEL 2 PROBLEMS
#FIND 33:
#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False
           
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
#Ok, this is what I had except for the -1 after nums, why is that there? Because nums[i+1] is saying to check if the next index matches, but if you're at the last
#element in the list, there's no next index, so it tosses an error. The -1 is the stop point in the range(start,stop,increment) function and stops the second to last
#element to avoid the error. We don't need to actually increment to the last element since we're checking it at the index before.

#BLACKJACK: Given three intergers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the sum by 10
#If they exceed 21 straight up, "BUST"

#Boring verson

def blackjack(*args):
    score = sum(args)
    for nums in args:
        if nums == 11 and score > 21:
            score -= 10
        if score == 21:
            return "You won!"
        elif score < 21:
            return score
        else:
            return 'BUST'
        
#Fun version:

import random

rand_list = [random.randint(0,11) for nums in range(0,3)]
print(rand_list)

#Random int from 0-11
def blackjack(rand_list):
    score = sum(rand_list)
    for nums in rand_list:
        if nums == 11 and score > 21:
            score -= 10
        if score == 21:
            return "You won!"
        elif score < 21:
            return score
        else:
            return 'BUST'

print(blackjack(rand_list))

