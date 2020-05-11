#Ryan Arnoldy 
# Fizz Buzz program
# If input / 3 return fizz 
# If input / 5 return buzz 
# If input / by 3 and 5 return fizzbuzz
# Otherwise return the original value to the user 


def fiz_buzz(input):
    if (input % 3 ==0) and  ( input % 5 ==0 ): 
        return "fizzbuzz"
    if input % 3 == 0: 
        return "fizz" 
    if input % 5 == 0: 
        return "buzz"
    return input

print(fiz_buzz(15))
