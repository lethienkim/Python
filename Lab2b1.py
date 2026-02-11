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
          annual_fuel_cost=float()
          tax_rate=float()
          total_house_cost=float()
          if (initial_cost>0):
               print("Inituial cost: $ ",initial_cost)
               annual_fuel_cost=float(input("Please input the Annual Fuel Cost: $ "))
               if (annual_fuel_cost>0):
                    print("Annual Fuel Cost: $ ",annual_fuel_cost)
                    tax_rate=float(input("Please input the Tax Rate: % "))
                    if (tax_rate>0):
                         #compute
                         total_house_cost=initial_cost+(annual_fuel_cost*5)+(tax_rate*initial_cost*5)
                    else:
                         print("You did not enter a valid Tax Rate number. ")
                         tax_rate=float(input("Please input the Tax rate again: %  "))   
               else:
                    print("You did not enter a valid Annual Fuel Cost number. ")
                    annual_fuel_cost=float(input("Please input the Annual Fuel Cost again: $  "))             
          else:
               print("You did not enter a valid Initial Cost number. ")
               initial_cost=int(input("Please input the Initial house cost again: $   "))                    
          #output
          print("Initial Cost:                 $ ",initial_cost)
          print("Annual Fuel Cost:             $ ",annual_fuel_cost)
          print("Tax Rate:                    ",tax_rate,"%")  
          print("Total House Cost for 5 years: $ ",total_house_cost)
          #See if the user wants to do another one
          keep_going = input('Do you want to calculate another ' + 'total house cost (Enter y for yes):')
main()
