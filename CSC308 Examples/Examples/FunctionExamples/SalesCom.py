# Ryan Arnoldy 
# Example Program from text
# Page 255    


def main(): 

    sales = Monthlysales() 
    Advpay = Advancedpay() 
    Comiss = SalesComiss(sales) 

    pay = sales * Comiss - Advpay 

    print("The pay is $", format(pay, '.2f'))

    if pay < 0: 
        print("The employee must pay:", format(Advpay, '.2f'))  




def Monthlysales(): 
   totalSales = int(input("Enter the employees sales for the month: "))
   return totalSales  

def Advancedpay(): 
    payAdvance = float(input("Enter the amount of advance pay that the employee recieved")) 
    return payAdvance

def SalesComiss(salesvalue):
    if salesvalue < 10000.00: 
        rate = 0.10 
    elif salesvalue >= 10000.00 and salesvalue <= 14999:
        rate = 0.12 
    elif  salesvalue >= 15000.00 and salesvalue <=17999:
        rate = 0.14 
    elif salesvalue >= 18000 and salesvalue <= 21999:
        rate = 0.16 
    else: 
        rate= 0.18
    return rate   
        
main()
        
