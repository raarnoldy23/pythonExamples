import random 

# 2Create a basic math program 
num1 = random.randint(1,10)
num2 = random.randint(1,10)


answer = num1 + num2 
print ('What is ', num1, '+', num2)

userAnswer = int (input('Enter your answer:'))

if userAnswer == answer: 
    print('Correct!!')
else: 
    print('Dumb ass the answer was', answer)

