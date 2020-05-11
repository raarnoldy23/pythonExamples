# Ryan Arnoldy 
# 3/20/20 

def main(): 
    # make a list containing even numbers 
    even_numbers = [2,4,6,8,10]
    odd_numbers = [1,3,5,7,9]
    numbers = even_numbers + odd_numbers  
    # len function  
    size = len(even_numbers) 
    # Display list
    print(even_numbers)
    print('The size is', size)
    print('The numbers are:', numbers) 
    


    # index loow with while
    i = 0 
    while i < 5: 
        print(even_numbers[i])
        i += 1


main()
