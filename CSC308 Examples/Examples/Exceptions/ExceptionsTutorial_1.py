# Ryan Arnoldy 
# 3/24/2020 
# demonstrates the use of the try/except block  

try:
    f = open('numbers.txt')
except FileNotFoundError:
    print('file not found!!')  
except Exception: 
    print('error!!')
else: 
    # only runs if we DONT throw and exception 
    print(f.read()) 
    f.close()  
finally: 
    # Runs regardless if an exception is thrown or not  
    print('Executing finally') 