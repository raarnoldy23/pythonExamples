# Ryan Arnoldy 
# Ex 7-6 Rainfall 
# 3/24/2020 
# Get the user input for the program 
# Calculate and display the Results
# Use Plot to Plot the results
import matplotlib.pyplot as plt 


def main():  
    months = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']  
    RainFallInput = GetRainFall(months)
    DisplayRainfall(months, RainFallInput)
    CalculateRainfall(RainFallInput)


# Function That gets the input from the user for rainfall for each month
def GetRainFall(month): 
    rainfall = []
    for num in month:  
        print('Enter the rainfall for:', num)
        rainFallEntered = float(input('Rainfall:'))
        rainfall.append(rainFallEntered)
    return rainfall


# Function That Calculates The Total RainFall
def CalculateRainfall(Rainfall): 
    TotalRainfall = 0 
    Length = len(Rainfall)
    for num in(Rainfall):  
        TotalRainfall = TotalRainfall + num   

    Avg = TotalRainfall / Length 
    return Avg, TotalRainfall   


# Function That displays the Total RainFall 
def DisplayRainfall(month, Rainfall):  
    # Calls Calculate Function Returns Average and total
    AverageRain, Total = CalculateRainfall(Rainfall) 
    index = 0 
    bar = 5
    monthsLength= len(month) 
    while index < monthsLength: 
        print('The Rainfall for', month[index], 'is', Rainfall[index])
        index += 1  
    print('The average is:', AverageRain)
    print('The total rain is', Total)

    # Plot the output 
    leftedges=[0,10,20,30,40,50,60,70,80,90,100,110]
    plt.bar(leftedges,Rainfall,bar)
    plt.ylabel('Inches of Rain')
    plt.xlabel('Months')
    plt.title('Rainfall by year')
    plt.xticks([5,15,25,35,45,55,65,75,85,95,105],month)  
    
    


    plt.show() 




main() 
         






