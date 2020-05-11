 # Ryan Arnoldy 
 # TipTaxTotal 
 # 1/30/2020
 # Exe 2-10


TAX = 1.07
Tip = 1.18 

Bill = float (input("What is the total bill amount?"))

#Calculate tax + tip
totalBill = (Bill*TAX) 
totalBill = (totalBill*Tip)

print ('The total cost is:',  format(totalBill, '.2f'))

