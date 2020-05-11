# Ryan Arnoldy   
# Writing numbers to a data file  


def main(): 

    # open a file 
    outfile = open('numbers.txt','w')

    num1 =int( input("write a number")) 
    num2 =int( input("write a number"))
    num3 =int( input("write a number"))

    # write numbers to file 
    outfile.write(str(num1) + '\n')
    outfile.write(str(num2) + '\n')
    outfile.write(str(num3) + '\n')

    outfile.close()  
    print("Data written to file" ) 




main() 

 







