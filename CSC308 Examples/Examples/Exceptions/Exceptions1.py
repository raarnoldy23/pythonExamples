# Demonstrates the use of try and except statments 


def main():
    total = 0

    try:
        infile = open('test.txt', 'r')

        # read and add values from the files

        for line in infile: 
            amount= float(line)
            total += amount  

        infile.close()
        print(format(total,'.2f'))

    except IOError: 
        print('Error while reading the file')
    except ValueError:
        print('Non-numeric data found!!')
    except: 
        print('An error occured ')  
        


main()


