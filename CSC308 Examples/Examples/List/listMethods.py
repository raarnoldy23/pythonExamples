# Ryan Arnoldy 
# 3/20/2020 
# Testing methods for list 


def main():
    # Define list  
    list = [] 
    # Prime read  
    again = 'y'

    while again == 'y' or again == 'Y': 
        item =  int(input('Enter a number: ')) 
        list.append(item)

        again = input('y = yes or enter any other key to quit')
    #sort my list
    list.sort() 
    print("The list is: ")
    for item in list: 
        print(item)




main() 
