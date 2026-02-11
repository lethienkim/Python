#
#program to compute the best buy out after five of three house presented
#It collects the inital cost

#name: Thienkim Le
#COSC 1336 Fundamentals of Programming
#ACC SPRING 2023
#lab2.py
#Professor Onabajo
#Global variable
year = 5
def main ():
    #variable declaration
    icost=0.0
    fuel_cost=0.0
    taxrate=0.0
    total_cost=0.0
    #using a loop to collect input from user
    k=0
    while (k<3):
        print("Please enter information for house: ",k+1)
        icost=float(input("Please input the Inital Cost: "))
        fuel_cost=float(input("Please input the Fuel Cost: "))
        taxrate=float(input("Please input the Tax Rate: "))
        #cumpute
        total_cost=icost+fuel_cost*year+icost*taxrate*year
        #output
        print("Initial Cost",icost)
        print('Total Cost', total_cost)
        #increment the counter
        k=k+1
    #hold screen
    dummy=input('Please press anykey to continue')
main()
        
    
