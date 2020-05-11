 # Ryan Arnoldy 
 # TipTaxTotal 
 # 1/30/2020
 # Exe 2-11


male = int(input('Enter number of males students:'))
female = int(input('Enter number of female students:'))
total = male + female 
totalFemale= (female/total)
totalMale = (male/total)

# Print Output
print('The percent female is:', format( totalFemale, '.0%'))
print('The percent make is:', format( totalMale, '.0%'))