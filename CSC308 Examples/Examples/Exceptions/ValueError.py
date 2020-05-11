# Ryan Arnoldy 
# 3/17/2020 
# Test the value 


def main ():
    try: 
        test = int(input("Enter a value"))
        print("You entered: ", test)

    except ValueError:
        print("Error")

main()  