#This program is process a structure known as Dictionary
#Part a of this will only compute a lsit of differnt types
#It will load the Dictionary and Query
#Part B will incorporate data into Dictioary also Query
#Name: ThienKim Le
#ACC Spring 2023
#Professor Onabajo
#COSC 1336 Fundamentals of Programming
#Lab6.py

#Global Variable
n=10
def main():
    #Dictionary Declaration
    restname=[" "]*10
    foodtype=[" "]*10
    reservation=[0]*10
    rating=[0]*n
    creditcards=[0]*n
    #File Declaration
    infile=open("Lab6a.txt",'r')
    outfile=open("Lab6.out",'w')
    #Call Function
    loadrec(infile,restname,foodtype,reservation,rating,creditcards)
    creditcard(outfile,restname,creditcards)
    chinese(outfile,restname,foodtype,rating)
    health(outfile,restname,foodtype)
    allstars(outfile,restname,rating)
    star(outfile,restname,rating)

    #close files
    infile.close()
    outfile.close()
    #Hold Screen
    dummy=input("Please enter anykey to continue: ")
    
def loadrec(file,a,b,c,d,e):
    #a=restname,b=foodtype,c=reservation,d=rating,e=creditcards
    #local Variable
    k=0
    while(k < n):
        templist=file.readline().strip('\n').split(',')
        a[k]=templist[0]
        b[k]=templist[1]
        c[k]=int(templist[2])
        d[k]=int(templist[3])
        e[k]=int(templist[4])
        k=k+1
def creditcard(outfile,a,b):
    #a=restname,b=creditcards
    #local variable
    k=0
    print ('\n',"Restuarants that take credit cards: ",'\n')
    outfile.write("Restaurants that take credit cards: ")
    while (k < n):
        if(b[k]==1):
            print(a[k])
            outfile.write(str(a[k])+"\n")
        k=k+1
def chinese(outfile,a,b,c):
    #a=restname,b=foodtype,c=rating
    #local variable
    k=0
    print('\n',"Restaurants that serve Chinese and three stars and above: ",'\n')
    outfile.write("Restaurants that serve Chinese and three stars and above: ")
    while k<n:
        if ((b[k]=="Chinese")and (c[k]>=3)):
            print(a[k])
            outfile.write(str(a[k])+"\n")
        k=k+1
def health(outfile,a,b):
    #a=restname,b=foodtype
    #local variable
    k=0
    print('\n',"Restaurants that serve Healthy foods: ",'\n')
    outfile.write("Restaurants that serve Health foods: ")
    k=0
    while k<n:
        if (b[k]=="Health"):
            print(a[k])
            outfile.write(str(a[k])+"\n")
        k=k+1
def allstars(outfile,a,b):
    #a=restname,b=rating
    #local variable
    j=0
    k=0
    while (j < 4):
        print ('\n',"Restuarants that are ",j+1,"star(s)",'\n')
        #outfile.write("Restaurants that are ",j+1,"star(s)")
        k=0
        while (k< n):
            if(b[k]==j+1):
                print(a[k])
                outfile.write(str(a[k])+ "\n")
            k=k+1
        j=j+1
def star(outfile,a,b):
    #a=restname,b=rating
    #local variable
    k=0
    print('\n',"Restaurants have at least one star and above: ",'\n')
    outfile.write("Restaurants have at least one star and above: ")
    k=0
    while k<n:
        if (b[k]>=1):
            print(a[k])
            outfile.write(str(a[k])+"\n")
        k=k+1
main()
    
    
