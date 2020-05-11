yes = True
Yes = True
no = False
No = False  
# Taken from internet
Rest1 = "Joe's Gourmet Burgers"                             #Not Veg, Not Vegan , Not Gluten-Free
Rest2 = "Main Street Pizza Company"                         #Yes veg, Not Vegan , Yes Gluten-Free
Rest3 = "Corner Cafe"                                       #Yes veg, Yes Vegan , Yes Gluten-Free
Rest4 = "Mama's Fine Italian"                               #Yes veg, Not Vegan , Not Gluten-Free
Rest5 = "The Chef's Kitchen"                                #Yes veg, Yes Vegan , Yes Gluten-Free
prompt = "Here are your restaurant choices:"

Vegan = str (input('Is anyone in your party vegan? Enter yes or no: '))
Vegetarian = str(input('Is anyone in your party vegetarian? Enter yes or no: '))
Glutenfree = str(input('Is anyone in your party Gluten Free? Enter yes or no: '))

if Vegan == 'yes' or 'Yes' and Vegetarian == 'yes' and Glutenfree == 'yes': 
    print('Your options are: \n The Chef\'s kitchen. \n Cafe\' corner.')
elif Vegan == 'yes' and Vegetarian == 'yes' and Glutenfree == 'no':
    print('Your options are: \n The chef\'s kitchen. \n Cafe\'e corner.')
elif Vegan == 'yes' and Vegetarian == 'no' and Glutenfree == 'no':
     print('Your options are: \n the chef\'s kitchen. \n Mama\'s fine Italian Kitchen \n Main Street Pizza. \n Corner Caf\'e  ')
elif Vegan == 'yes' and Vegetarian == 'no' and Glutenfree == 'yes':
    print(prompt, Rest2, Rest3 , Rest5 ) 
elif Vegan == 'yes' and Vegetarian == 'no' and Glutenfree=='yes': 
    print(prompt, Rest2, Rest3, Rest5)
elif Vegan == 'yes' and Vegetarian == 'no' and Glutenfree=='no': 
    print(prompt,Rest2, Rest3, Rest5 )
elif Vegan == 'no' and Vegetarian == 'no' and Glutenfree=='yes': 
    print(prompt,Rest2, Rest3, Rest5 )
elif Vegan == 'no' and Vegetarian == 'no' and Glutenfree=='no':
    print(prompt, Rest1, Rest2, Rest3, Rest4, Rest5)
else: 
    print('Select and option')

    