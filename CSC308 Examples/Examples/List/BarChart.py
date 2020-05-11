# Ryan Arnoldy 
# 3/24/2020
# Working with Matplotlib 
import matplotlib.pyplot as plt 

def main():
    values = [23,33,55,45,21,65]
    leftEdges = [0,10,20,30,40,50]
    barwidth = 5

    # Plot Bar graph 
    plt.bar(leftEdges,values,barwidth, color=('r','b','k','m','c','y')) 

    #Bar graph titles
    plt.title('Test Title')
    plt.xlabel('This is the x axis')
    plt.ylabel('This is the y label')





    # Pie chart
    #plt.pie(values)


    plt.show()


main()