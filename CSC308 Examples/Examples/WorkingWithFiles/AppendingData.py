# Appending data to a file  
# 3/14/2020 


def main():
    # open file object  and set mode 
    myfile = open('hello.txt', 'a')
    myfile.write("adding data to file\n")
    myfile.write("Adding 1\n ")
    myfile.close()   
 


main()