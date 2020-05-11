
keep_going = 'y' 
budgetValue = float (input('Enter the total you have budgeted.'))
while keep_going =='y':  
    expence = float(input('Enter your expense: '))
    budgetValue = budgetValue - expence
    print('Your current balence is: ', '$', budgetValue)
    keep_going = input('Would you like to continue? Press y for yes')

print('Your final value is:', budgetValue) 

