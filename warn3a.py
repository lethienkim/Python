# Program to load from a data file and to write to an output file
# Name: ThienKim Le
# warm3a.py
# Golbal variable
n=10
def main():
    # file declaration
    infile=open("warm3a.txt",'r')
    outfile=open("warm3a.out",'w')
    # varible declaration
    a=b=c=d=e=f=g=h=i=j=0
    # yank/read from the data file
    templist=infile.readline().strip('\n').split(',')
    # convert from string to integer
    a=int(templist[0])
    b=int(templist[1])
    c=int(templist[2])
    d=int(templist[3])
    e=int(templist[4])
    f=int(templist[5])
    g=int(templist[6])
    h=int(templist[7])
    i=int(templist[8])
    j=int(templist[9])
    # show teplist in the memory
    print(templist)
    # write to the screen
    print(a,b,c,d,e,f,g,h,i,j)
    # write to the output file
    outfile.write(str(a)+'\t'+str(b)+" "+str(c)+" "+str(d)+" "+str(e)\
                   +str(f)+" "+str(g)+" "+str(h)+" "+str(i)+" "+str(j))
    # close file
    infile.close()
    outfile.close()
    # hold screen
    dummy=input("Please enter anykey to continue: ")
main()                  
    
    
    
