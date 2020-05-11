# Ryan Arnoldy 
# Program  textbook 

# cost for seats: 
A_COST = 20
B_COST = 15
C_COST = 10


def main(): 
    class_A = int(input("How manay class A seats? "))
    class_B = int(input("How many class B seats? "))
    class_C = int(input("How many class C seats? "))

    calculate(class_A, class_B, class_C)  


def calculate(Seats_A, Seats_B, Seats_C): 
    total_A = Seats_A * A_COST
    total_B = Seats_B * B_COST 
    total_C = Seats_C * C_COST 
    
    total = total_A + total_B + total_C 

    #show the user results
    print ("The total is $", total)


# call to the main function to start the program     
main() 
