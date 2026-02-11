#Warm36.py
#Program to call a function
#Mname : ThienKim Le
#Global variable
n=2
def main ():
    #local variable
    a=b=c=d=0
    a=2
    b=-3
    c=3
    #call the function Dallas
    d=Dallas(a,b,c)
    #output
    print(a,b,c,d)
    #hold screen
    dummy=input("Please enter anykey to continue:")
    #end main
def Dallas(r,s,t):
    #local variable
    a=4
    b=0
    #calculate
    b=r+s*t+n-a
    return(b)
main()
