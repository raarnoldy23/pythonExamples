# Ryan Arnoldy
# Ex 6-7 
import random 

def main(): 
    numbers = int(input("How many random numbers do you want to write? "))

    outfile = open('random.txt','w')

    # Write the specified number of random numbers to the file 
    for num in range(1,numbers+1): 
        number = rand() 
        # Write the value to the file 
        outfile.write(str(num) + ". ")
        outfile.write( str(number) + "\n")  

    # Call function to close the file 
    close(outfile)


# Function the closes the file    
def close(file):
    file.close() 
    print("Data written closing file")


# function returns random number 
def rand(): 
    num = random.randint(1,500)
    return num
     

# call main      
main() 








