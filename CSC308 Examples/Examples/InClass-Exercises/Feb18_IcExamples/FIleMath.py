total =0 
acc = 0 
Data = open('numbers.txt', 'r')

for line in Data:  

    numbers = int(line)
    total += numbers
    acc += 1 
    
avg = total/acc    

Data.close()  

#print(fileData)
print('The total is:',  total)
print('The average is:', avg)
