#
#Lab3
#Name:ThienKim Le
#COSC 1336-Spring 2023-TR9am
#Prof: Onabajo

# Calculate Batting & Slugging Average
n=9
import baseball

def main():
    #instantiate a new class baseball
    base=baseball.baseball()
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
        print('player','','single','','Double','','triple','','homerun','','atbat')
        print('  ',p,"    ",s,"      ",d,"     ",t,"   ",hr,"     ",atbat)
        #compute
        s1=base.single(s)
        d1=base.double(d)
        t1=base.triple(t)
        hr1=base.homerun(hr)
      
        ba=round(float(s+d+t+hr)/atbat,2)
        sa=round(float((s*1)+(d*2)+(t*3)+(hr*4))/atbat,2)
        #sa=float((s1+d1+t1+hr1)/(atbat)
        #print(p,format(ba,'.2f'),'\t',format(sa,'.2f'))
        #outfile.write(str(p)+str(format(ba,'.2f')),'\t',str(format(sa,'.2f'))+\n')
        #output 
        print ("       ",s1,"       ",d1,"       ",t1,"   ",hr1,"    ",atbat,'\n'
               "Bat Average:      ",ba,"\n"
               "Slugging Average: ",sa,"\n")
        k=k+1
    #close file
    infile.close()
    outfile.close() 
    
    dummy=input("Please enter any key to continue: ")
    #end main
main()
