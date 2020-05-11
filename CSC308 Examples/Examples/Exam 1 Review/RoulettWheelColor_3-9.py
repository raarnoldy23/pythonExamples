pocket = int(input('Choose a pocket 0-36:')) 

if pocket == 0: 
    print('The pocket is green!')
elif pocket > 0 and pocket < 10:
    if (pocket%2) == 0:
        print('The pocket is black!')
    else:
         print('The pocket is red!') 
elif pocket > 10 and pocket <= 18:
    if(pocket%2)==0: 
        print('The pocket is red!')
    else:
        print('The pocket is black!')
elif pocket > 18 and pocket <= 28: 
    if (pocket%2)==0: 
        print('The pocket is black!')
    else: 
        print('The pocket is red!')
elif pocket > 28 and pocket <= 36: 
    if (pocket%2)==0: 
        print:('The pocket is red!')
    else: 
        print('The pocket is black!')
else:
    print('Please enter a valid value!!')
