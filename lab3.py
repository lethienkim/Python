#Lab3
#Name:ThienKim Le
#COSC 1336-Spring 2023-TR9am
#Prof: Onabajo
# Calculate Batting & Slugging Average
n=9
def main():
    #file declaration
    infile=open("lab3data.txt",'r')
    outfile=open("lab3data.out",'w')
    #varible declaration
    p=s=d=t=hr=atbat=0
    s1=d1=t1=hr1=at=0
    k=0
    sa=0.0
    ba=0.0
    while (k<n):
        #yank/read from the data file
        templist=infile.readline().strip('\n').split(',')
        #covert from string to interger
        p=int(templist[0])
        s=int(templist[1])
        d=int(templist[2])
        t=int(templist[3])
        hr=int(templist[4])
        atbat=int(templist[5])
        #write to the output file
        outfile.write(str(p)+'\n'+str(s)+" "+str(d)+""+str(t)+" "+str(hr)+" "+str(atbat))
        #write templist to the screen
        print(p,"  ",s,"  ",d,"  ",t,"  ",hr,"  ",atbat)
        #compute
        s1=single(s)
        d1=double(d)
        t1=triple(t)
        hr1=homerun(hr)
      
        ba=round(float(s+d+t+hr)/atbat,2)
        sa=round(float((s*1)+(d*2)+(t*3)+(hr*4))/atbat,2)

        #output
        print ("    ",s1,"  ",d1,"  ",t1,"  ",hr1,"  ",atbat,'\n'
               "Bat Average:      ",ba,"\n"
               "Slugging Average: ",sa,"\n")
        k=k+1
    #close file
    infile.close()
    outfile.close() 
    
    dummy=input("Please enter any key to continue: ")
    #end main
def single(x):
    #local variable
    y=0
    y=x*1
    return(y)
def double(x):
    y=0
    y=x*2
    return(y)
def triple(x):
    y=0
    y=x*3
    return(y)
def homerun(x):
    y=0
    y=x*4
    return(y)

main()
