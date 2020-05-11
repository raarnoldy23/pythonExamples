day = int(input('Enter a number 1-7 Monday is 1 Sunday is 7:'))

if day < 1 or day > 7: 
    print('Enter a valid number 1 through 7.')
elif day == 1:
    print('Monday.')
elif day== 2:
    print('Tuseday.')
elif day == 3:
    print('Wednesday.')
elif day== 4:
    print('Thursday.')
elif day == 5:
    print('Friday.')
elif day == 6:
    print('Saturday')
else:
    print('Sunday.')