# program to load 2-list and to manipulate the list
#Also to cpmpute the largest
#name: Thienkim Le
#COSC 1336 Fundamentals of Programming
#ACC SPRING 2003
#Warm5a
#Professor Onabajo
#Global variable
large=0
def main():
    # file declaration
    infile=open("warm5a.txt",'r')
    outfile=open("warm5a.txt",'w')
    # List declaration
    x=[[0,0,0],
       [0,0,0],
       [0,0,0]]
    # local variable
    suma=0
    # call function
    loadrec(infile,x)
    suma=sumation(x)
    largest(x)
    outdata(outfile,x)
    print("Suma = ",suma)
    print("Largest = ",largest)
    # close file
    infile.close()
    outfile.close()
    # hold screen
    dummy=input('\nPlease enter anykey to continue:')
    # function
def loadrec(file,a):
    #a=x 
    #local avariable
    s=0
    #load row
    k=0
    j=0
    n=0
    #counter for templist
    templist=file.readline().strip('\n').split(',')
    while j<3:
        k=0
        while k<3:
            a[k][j]=int(templist[n])
            k=k+1
            n=n+1
        j=j+1
def sumation(a):
    # Sumation of column 2
    s=0
    k=0
    while k<3:
        s=s+a[k][1]
        k=k+1
    return(s)
def large(a):
    # global avarible
    global large
    k=0
    large=a[1][k]
    while k<3:
       if (large<a[1][k]):
           large = a[1][k]
       k=k+1
def outdata(file,a):
    #local variable
    #a=x
    k=0
    while k<3:
        print(a[k][0],a[k][1],a[k][2])
        file.write(str(a[k][0])+'    '+str(a[k][1])+'    '+str(a[k][2])+'\n')
        k=k+1
main()
       
