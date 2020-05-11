# Ryan Arnoldy 
# 3/24/2020
# Python Example  7-6

def main(): 
    List = Input() 
    Value = greaterThan()

    for num in List: 
        if num > Value:55
            print(num)
    

def Input(): 
    Userinput = [] 
    again = 1
    while again !=0 : 
        numbers = int(input('Enter an integer 0 to quit: '))
        Userinput.append(numbers)  
        #again = input('Run again? Y/y or any other key to quit.') 

    return Userinput


def greaterThan():
    value = int (input('Enter a value to display list values that are greater than: '))
    return value 
    


main()

    
    

