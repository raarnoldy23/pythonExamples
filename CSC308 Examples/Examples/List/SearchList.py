# Ryan Arnoldy 
# 3/20/2020 
# Searching list 


def main(): 
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    search = int(input('Enter a number to search:'))
    
# search list
    if search in list: 
        print('found', search, 'in list')

    else:  
        print('Could not find', search)



main()   




