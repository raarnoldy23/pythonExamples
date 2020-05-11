# Ryan Arnoldy 3/7/2020 
# Demonstrates the use of functions and random 

import random
import time 

MIN = 1
MAX = 6 


def main(): 
    totalCount = 5 
    while totalCount != 0: 
       
        # function that gets user answer
         user = guess() 
        # function that rolls dice
         dice = roll()  
        # function that compares user answer to dice 
         answer = checkAnswer(user, dice) 
        # function to calculate new total 
         totalCount = Score(answer,totalCount)
         if totalCount == 10: 
            print("YOU WON!!")
    print("You lose!!!")

    
# Function to roll the dice
def roll():
    dice = random.randrange(MIN, MAX)
    print("The roll was") 
    time.sleep(1)
    print(dice)
    return dice  


# Function to accept user guess
def guess(): 
    user_guess = int (input("Please select a number between 1 and 6:")) 
    print('The user guess is: ', user_guess)
    return user_guess 


# Function compares values to 
def checkAnswer(user,com):
    if user == com: 
        answer = True
    else:
        answer = False
    return answer  
  
     
# Function to calculate points
# input is the return value from answer function 
# total is the point total
def Score(input,total):
    if input == True: 
        total = total + 1 
        print("you win the new total is", total)
        
    else: 
        total = total - 1
        print("you lose the new total is", total)
    return total 


main() 








