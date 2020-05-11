# Ryan Arnoldy 
# 3/24/2020
# Raising custom exceptions  


try:
    value = int(input('Enter a value less than 10: '))
    if value > 10:
        raise Exception 
except Exception:  
    print('Please enter a valid number')
except
else:
    value = int(input('Enter a value less than 10: '))
    if value > 10:
        raise Exception 
print('Thank you!!')