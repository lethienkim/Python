     #
#program to compute the total cost of the house after 5 years
#
#name: Thienkim Le
#COSC 1336 Fundamentals of Programming
#ACC SPRING 2003
#lab2.py
#Professor Onabajo
def main():
     keep_going='y'
      #promt user for input
     while keep_going =='y':
          initial_cost=int(input("Please input the Initial house cost: $"))
          annual_fuel_cost=float(input("Please input the Annual fuel cost: $"))
          tax_rate=float(input("Please input the Tax rate: %")) 
          if (initial_cost<=0):
               print("You did not enter a valid number.")
               initial_cost=int(input("Please input the Initial house cost again:   "))  
               annual_fuel_cost=float(input("Please input the Annual fuel cost:  "))
               if (annual_fuel_cost<=0):
                    print("Inituial cost:    $ ",initial_cost)
                    print("You did not enter a valid number. ")
                    annual_fuel_cost=float(input("Please input the Annual fuel cost again:  "))
                    tax_rate=float(input("Please input the Tax rate:   "))
               if (tax_rate<=0):
                    print("Inituial cost:    $ ",initial_cost)
                    print("Annual Fuel Cost: $ ",annual_fuel_cost)
                    print("You did not enter all valid numbers. ")
                    tax_rate=float(input("Please input the Tax rate again:  ")) 
          #compute
          total_house_cost=initial_cost+(annual_fuel_cost*5)+(tax_rate*initial_cost*5)
          #output 
          print("Inituial cost:                $ ",initial_cost)
          print("Annual Fuel Cost:             $ ",annual_fuel_cost)
          print("Tax Rate:                    ",tax_rate,"%")  
          print("Total House Cost for 5 years: $ ",total_house_cost)
          #See if the user wants to do another one
          keep_going = input('Do you want to calculate another ' + 'total house cost (Enter y for yes):')
main()
