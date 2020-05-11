# Ryan Arnoldy 
# Ex 5-8 Painter Estimate 
# 3/10/2020

HOURLYRATE = 35.00 

def main(): 
    square_feet = float(input("How many square feet do your need painted?"))
    paint_cost = float(input("What is the cost of the paint per gallon?"))
    calculatCost(square_feet, paint_cost)

def calculatCost(area,cost):
    totalPaint = area / 112  
    totaltime = (area / 112) * 8  
    Labor = totaltime * HOURLYRATE 
    paintCost = totalPaint * cost
    totalCost = paintCost + Labor 

    print("Your will need", totalPaint, "gallons ")
    print("It will take", totaltime, "hours")
    print("The cost of paint will be $", paintCost)
    print("Labor cost will be $", Labor)
    print("The totalCost will be $", totalCost)

main()