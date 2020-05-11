# Ryan Arnoldy 
# 3/20/2020/ 
# Example 7.1 from text 
# Get sales 


def main(): 
    sales = [] 
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    total = 0 
    index = 0 
    daysSize = len(days)
    while index < daysSize:
        print('Enter sales for', days[index])
        daily_sales = float(input('Enter sales:',  ))
        sales.append(daily_sales) 
        total += daily_sales  
        index += 1 
    results(days, sales, total)

    #print("The total is:$", total)


def results(day, sales, total): 
    index = 0 
    saleLen = len(sales) 
    while index < saleLen: 
        print('The Sales for', day[index], '$', sales[index])
        index += 1  
    print('The total for the week is: $', total)





main()   
        






