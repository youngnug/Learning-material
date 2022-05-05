from random import shuffle
#Ball in cup
balls = ['','O','']
#Shuffle ball function
def shuffle_list(balls):
    shuffle(balls)
    return balls
#Player guess function using input of index positions (have to convert string to int)
def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0, 1, or 2: ")
    return int(guess)
#Assign varibale for result of shuffle and result of guess
shuffle_result = shuffle_list(balls)
guess_index = player_guess()
#Function to check if the result of shuffle at index of player guess equals the ball ('O')
def guess_result(shuffle_result,guess_index):
    if shuffle_result[guess_index] == 'O':
        print("You gussed corretly!")
        print(shuffle_result)
    else:
        print("You guessed incorrectly!")
        print(shuffle_result)

#Function calls
#Initial list
balls = ['','O','']
#shuffle the list
shuffle_list(balls)
#check if its a correct guessed
guess_result(shuffle_result,guess_index)
