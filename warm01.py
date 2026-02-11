#This program is to compute the sum average
# of any 10 number. Will prompt use tone by one
# Also will computer sum and average
# Name: Thienkim Le
# COSE 1336 Python Programming
# ACC Spring 2023
# warm01.py
# Prof Onabajo
def main ():
    # Variable declaration
    avg=0.0
    sumx=0.0
    num=0
    k=0
    # Promt user for input using a loop
    while (k<10):
        num=int(input("Pls enter a number     "))
        # add num to sum
        sumx=sumx+num
        # increment k
        k=k+1
    # comupter average
    avg=sumx/10
    #output
    print("THE SUM =   ",sumx)
    print("AVERAGE =    ",avg)
main()
    
