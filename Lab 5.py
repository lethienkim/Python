# program to manipulate matrices 2-list
# Will load matrices, multiply matrices, add matrices
# also will compute the smallest and print out entire matrices
# Jonathan Valencia
# COSC 1336 Programming fundamentals using python
# ACC spring 2023
# Lab 5.py
# Professor Onabajo

# Global variable
small=0
sumx=0
sumy=0
zmatrices=0
def main():
    # file declaration
    infilex=open("lab5x.txt",'r')
    infiley=open("lab5y.txt", 'r')
    outfile=open("lab 5.out",'w')


    # list declaration
    # x[5][3]
    x=[[0,0,0],
       [0,0,0],
       [0,0,0],
       [0,0,0],
       [0,0,0],]
    #y[3][7]
    y=[[0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0]]
    #z[5][7]
    z=[[0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0]]
    # Variable declaration
    # small=0
    # call functions
    loadx(infilex, x)
    loady(infiley, y)
    ZMatrices = computez(x, y, z)
    sumx = summationx(x)
    sumy = summationy(y)
    small = smallest(y)
    outdata(outfile, x, y, z)

    # print the rest of the output
    print('\n'"Array Z:")
    print_matrix(ZMatrices)
    outfile.write("Zmatrices= " + str(ZMatrices))
    print('\n'"Smumx = ", sumx)
    outfile.write("Sumy = " + str(sumx))
    print("Sumy= ", sumy)
    outfile.write("Sumy = " + str(sumy))
    print("Sumx+Sumy= ", sumx + sumy)
    outfile.write("Sumx+Sumy= " + str(sumx + sumy))
    print("Smallest = ", small)
    outfile.write("Smallest = " + str(small))
    infilex.close()
    infiley.close()
    outfile.close()

    # hold screen
    dummy = input('\nPlease enter anykey to continue:')


def loadx(file, a):
    # c=z[5][7]
    s = 0
    # load row
    k = 0
    j = 0
    n = 0
    # counter for templist
    templist = file.readline().strip('\n').split(',')

    while k < 5:
        j = 0
        while j < 3:
            a[k][j] = int(templist[n])
            j = j + 1
            n = n + 1
        k = k + 1


def loady(file, b):
    # b=y[3][7]
    s = 0
    # load row
    k = 0
    j = 0
    n = 0
    # counter for templist
    templist = file.readline().strip('\n').split(',')
    while j < 7:
        k = 0
        while k < 3:
            b[k][j] = int(templist[n])
            k = k + 1
            n = n + 1
        j = j + 1


def computez(a, b, c):
    # variable declaration
    # x[5][3],y[3][7],z[5][7]
    i = 0
    j = 0
    k = 0
    # using 3 loops to mutipu x & y to get z
    i = 0
    while i < 5:
        j = 0
        while j < 7:
            k = 0
            while k < 3:
                c[i][j] = c[i][j] + a[i][k] * b[k][j]
                k = k + 1
            j = j + 1
        i = i + 1

    return (c)


def summationx(a):
    # Sumation of column 3 of X-Matrix
    s = 0
    k = 0
    while k < 5:
        s = s + a[k][2]
        k = k + 1
    return (s)


def summationy(b):
    # Sumation of row 3 of Y-Matrix
    s = 0
    j = 0
    while j < 7:
        s = s + b[2][j]
        j = j + 1
    return (s)


def smallest(b):
    global small
    k = 0
    small = b[1][k]
    while k < 7:
        if (small > b[1][k]):
            small = b[1][k]
        k = k + 1
    return (small)


def outdata(file, a, b, c):
    # local variable
    # a=x[5][3],b=y[3][7],c=z[5][7]
    # b=y
    k = 0
    print('\n'"X-Matrics: ")
    while k < 5:
        print(a[k][0], a[k][1], a[k][2])
        file.write(str(a[k][0]) + '    ' + str(a[k][1]) + '    ' + str(a[k][2]) + '\n')
        k = k + 1
    print('\n'"Y-Matrics: ")
    k = 0
    while k < 3:
        print(b[k][0], b[k][1], b[k][2], b[k][3], b[k][4], b[k][5], b[k][6])
        file.write(str(b[k][0]) + '    ' + str(b[k][1]) + '    ' + str(b[k][2]) + '    '
                   + str(b[k][3]) + '    ' + str(b[k][4]) + '    ' + str(b[k][5]) + '    ' + str(b[k][6]) + '\n')
        k = k + 1


def print_matrix(m):
    row = 0
    while row < len(m):
        col = 0
        while col < len(m[row]):
            print(m[row][col], "", end='')
            col += 1
        print()
        row += 1
main()

































        
