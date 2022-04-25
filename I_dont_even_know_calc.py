import random
print('Hello, think of a random number between 1 and 100!')

list_of_evens = []
list_of_odds = []

for nums in range(1,101):
    list_of_evens.append(nums)
    if nums %2 != 0:
        list_of_evens.remove(nums)

for nums in range(1,101):
    list_of_odds.append(nums)
    if nums % 2 == 0:
        list_of_odds.remove(nums)

guess = random.randint(1,101)

while True:
    print(f"Is your number {guess}?")
    answer= input('Please Enter:\nYes\nHigher\nLower')
    if answer == 'yes':
        print("I'm so smart!")
        break
    elif answer == 'higher':
        guess +=1
        answer = input('Is your number even?')
        if guess%2 != 0:
            guess += 1
        if answer =='yes':
            print(list_of_evens[(list_of_evens.index(guess))::])
        
    elif answer == 'lower':
        guess -= 1
        answer = input('Is your number even?')
        if guess%2 != 0:
            guess -= 1
        if answer =='yes':
            print(list_of_evens[:(list_of_evens.index(guess))])
