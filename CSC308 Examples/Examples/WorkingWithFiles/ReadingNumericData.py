# Ryan Arnoldy 
# 3/14/2020   
# File that reads numeric data from a file

def main(): 
    infile = open('numbers.txt','r')
    
    # Read in the values 
    value_1 = int(infile.readline())
    value_2 = int(infile.readline())
    value_3 = int(infile.readline())

    sum = value_1 + value_2 + value_3
    
    print(sum) 

main()   
  