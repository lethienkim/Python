# Program to sort a set of IDs and Scores using Bubble sort Method
# It willread from a data file and write sorted data into an output file
# Also will call a Binary Search to modify data set
# Name: Thienkim Le
# COSC 1336
# ACC Spring 2023
# Lab7b.py
# Prof Onabajo

#global variable
n=20
def main():
    #list declaration
    ids=[0]*n
    score=[0]*n
    #file declaration
    infilex=open("lab7a.txt",'r')
    infiley=open("lab7b.txt",'r')
    outfile=open("lab7.out",'w')

    #call function
    print("Print out the ids and score: ")
    loadx(infilex,ids,score)
    outdata(outfile,ids,score)
    print('\n')
    print("Sorting the ids and score: ")
    bubble(ids,score)
    outdata(outfile,ids,score)
    print('\n')
    print("Sorting & Modifies data: ")
    binary(infiley,ids,score)
    outdata(outfile,ids,score)

    #close files
    infilex.close()
    outfile.close()
    #hold screen
    dummy=input("Please enter anykey to continue: ")

def loadx(file,a,b):
    #a=ids,b=score
    #local variable
    k=0
    while k<n:
        #yank the data
        templist=file.readline().strip('\n').split(',')
        a[k]=int(templist[0])
        b[k]=int(templist[1])
        k=k+1
def outdata(file,a,b):
    #a=ids,b=score
    #local variable
    k=0
    while k<n:
        #yank the data
        print("  ",a[k],b[k])
        file.write(str(a[k])+str(b[k])+'\n')
        k=k+1  
def bubble(a,b):
    #a=ids,b=score
    i=n-1
    flag=1
    while ((i>=1)and (flag==1)):
        j=0
        while (j<=i-1):
            if (a[j]>=a[j+1]):
                #swapping for ids
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
                #swapping for score
                temp1=b[j]
                b[j]=b[j+1]
                b[j+1]=temp1
                j=j+1
            else:
                j=j+1
        i=i-1

def binary(file,a,b):
    #a=ids,b=score
    #variable declaration
    flag=0
    low=0
    high=n
    k=0
    #loading from a modified data set
    while k<5:
        low=0
        high=n-1
        flag=0
        idn=0
        scn=0
        templist=file.readline().strip('\n').split(',')
        idn=int(templist[0])
        scn=int(templist[1])
        while low<high and flag==0:
            mid=int((low+high)/2)
            if a[mid]==idn:
                flag=1       
                print("Search Modify Sucessful:")
                #change the score
                b[mid]=scn
                
            elif a[mid]<idn:
                #high=mid-1
                low=mid+1
            else:
                #low=mid+1
                high=mid-1
        k+=1

main()








    
