seconds = float (input('How may seconds do you want to convert? '))

if seconds >= 60 : 
   minutes = seconds//60
   remhours = seconds %60 
   print('That is',format(minutes, '.0f'), ' minute and', format(remhours, '.3f'),'seconds')
elif seconds >= 3600 :
    hours = seconds // 3600 
    minutes = (seconds//60)%60 
    seconds = seconds %60
    print('That is ', hours, 'hours', minutes, 'minutes and', seconds, 'seconds!!')
else: 
    print('Not valid input!!!!!')

    