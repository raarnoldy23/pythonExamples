# Ryan Arnoldy 
# Example 3-2 
# Calculate and compare the area of two rectangles then compares which it bigger

# Input
L1 = float(input('Enter L1:'))
W1 = float(input('Enter W1:'))
L2 = float(input('Enter L2:'))
W2 = float(input('Enter W2:'))

# Calculate
Area1 = L1* W1
Area2 = L2* W2 

# Compare areas 
if Area1 == Area2:
    print ('The areas are equal.')
elif Area1 > Area2:
    print ('Area 1 is larger.', 'Area 1 is:', Area1)
else: 
    print ('Area 2 is larger.', 'Area 2 is:', Area2)




