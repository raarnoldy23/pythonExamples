# Working with functions
# Keyword
# Make a parameter optional

# by is set to 1 by default
# Optional parameters should be after required parameters 
def increment(number, by=1): 
    return number+by 

#creating multiple arguments   
def multiply(*numbers):
    #print(numbers)
    total = 1
    for number in numbers: 
        total *= number
    return total  

# Function Calls
print( increment(2,1))

# Using keyword arguments  
print(increment(2, by= 5))
#print(increment(2))


multiply(2,3,4,5)




