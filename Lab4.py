#Program to compute standard deviation and standard score
#It uses fllists function and data file
#Name: Thienkim Le
#COSC 1336 Fundamentals of Programming
#ACC Spring 2023
#Lab4a.py

#Gobal varibale
n=20
import math
def main():
    print("\n")
    #list declaration
    x=[0]*n
    dev=[0.0]*n
    dev1=[0.0]*n
    sd1=[0.0]*n
    #file declaration
    infile=open("warm4a.txt","r")
    outfile=open("warm4a.out","w")
    #variable declaration
    sumx=0.0
    std=0.0
    xbar=0.0
    dev2=0.0
    sd2=0.0   
    #call functtion 
    sumx=loadrec(infile,x)
    #compute the average
    xbar=sumx/n
    #call function deviation
    dev2=deviation(x,dev,dev1,xbar)
    #compute standard deviation
    std=math.sqrt(dev2/n)
    #call function stdscore
    sd1=stdscore(dev, std, sd1)
    sd2=sum(sd1)
    #call outdata
    outdata(outfile,x,dev,dev1,sd1,sd2)
    print("\nSum =", sumx)
    print(f'Average = {xbar:,.2f}.')
    print(f'Standard Deviation = {std:,.2f}.')
    print(f'Sum of Standard Score = {sd2:,.2f}.')
    
    #close files
    infile.close()
    outfile.close()
    #hold screen
    dummy=input("\nPlease enter anykey to continue:")

    #function
def loadrec(infile,a):
    #local variable
    k=0
    s=0
    while (k<n):
        #read the first line of data
        templist=infile.readline().strip('\n').split(',')                
        a[k]=int(templist[0])
        s=s+a[k]
        k=k+1
    return(s)
def deviation(a,b,c,d):
    #a=x b=dev c=dev1 d=xbar
    #loclal variable
    k=0
    s=0
    while (k<n):
        b[k]=d-a[k]
        c[k]=b[k]*b[k]
        s=s+c[k]
        k=k+1
    return(s)
def stdscore(dev, sdev, sd1):
    k=0  
    while k < n:
        sd1[k] = dev[k] / sdev
        k = k + 1
    return(sd1)
    
def outdata(file,a,b,c,d,e):
    #local variable
    #file=outfile,a=x,b=dev,c=dev1,d=sd1
    k=0
    while (k<n):
        print(a[k]," ",f'{b[k]:,.2f}.',"    ",f'{c[k]:,.6f}.',"       ",f'{d[k]:,.6f}.')
        file.write(str(a[k])+"    "+str(b[k])+"  "+str(c[k])+"    "+str(d[k]))
        k=k+1
main()    
        
