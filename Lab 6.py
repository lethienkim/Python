# This program is process a structure know as Dictionary
# Part A of this will only computer a list of different types
# It will load the dictionary and Query
# Part B will incorporate data into Dictionary also Query
# Jonathan Valencia
# Acc Spring 2023
# COSC 1336 Fundamentals of Programming using python
# Lab6.py
# Professor Onabajo

# Global Variable
n = 10


def main():
    # Dictionary declaration
    restname = [""] * 10
    foodtype = [""] * 10
    reservation = [0] * 10
    rating = [0] * n
    creditcards = [0] * n
    # file declaration
    infile = open("Lab6a.txt", 'r')
    outfile = open("Lab6.out", 'w')
    # Call Function
    loadrec(infile, restname, foodtype, reservation, rating, creditcards)
    creditcard(outfile, restname, creditcards)
    chinese(outfile, restname, foodtype, rating)
    health(outfile, restname, foodtype)
    allstars(outfile, restname, rating)
    stars(outfile, restname, rating)
    # close files
    infile.close()
    outfile.close()
    # Hold screen
    # dummy = input("Please enter any key to continue")


def loadrec(file, restname, foodtype, reservation, rating, creditcards):
    # a=restname, b=foodtype, c=reservation, d=rating, e=creditcards
    # local variable
    k = 0
    while k < n:
        templist = file.readline().strip('\n').split(',')
        restname[k] = templist[0]
        foodtype[k] = templist[1]
        reservation[k] = int(templist[2])
        rating[k] = int(templist[3])
        creditcards[k] = int(templist[4])
        k = k + 1
    print(restname)


def creditcard(outfile, restname, creditcards):
    # a=restname, b=creditcards
    # local variable
    k = 0
    print("Restaurant that accepts Credit Cards")
    outfile.write("Restaurants that accept Credit Cards\n")
    while k < n:
        if creditcards[k] == 1:
            print(restname[k])
            outfile.write(str(restname[k]) + "\n")
        k = k + 1


def chinese(outfile, restname, foodtype, rating):
    # a=restname, b=foodtype, c=rating
    # local variable
    k = 0
    print("Restaurant that serve Chinese and three stars and above")
    outfile.write("Restaurants that serve Chinese and 3 stars and above\n")
    for k in range(len(restname)):
        if (foodtype[k] == 'Chinese') and (rating[k] not in (1, 2)):
            print(restname[k], "\n")
            outfile.write(str(restname[k]) + "\n")
            k = k + 1


def health(outfile, restname, foodtype):
    # a=restname, b=foodtype,
    # local variable
    k = 0
    print("Restaurant that serve Health")
    outfile.write("Restaurant that serve Health\n")
    for k in range(len(restname)):
        if foodtype[k] == 'Health':
            print(restname[k], "\n")
            outfile.write(str(restname[k]) + "\n")
        k = k + 1


def allstars(outfile, restname, rating):
    # a=restname, b=rating
    # local variable
    k = 0
    print("Restaurant that are 4 stars or above")
    outfile.write("Restaurant that are 4 stars or above\n")
    for k in range(len(restname)):
        if rating[k] not in (1, 2,3):
            print(restname[k], "\n")
            outfile.write(str(restname[k]) + "\n")
        k = k + 1


def stars(outfile, restname, rating):
    # a=restname, b=rating
    # local variable
    k=0
    print("Restaurant that are 3 stars or less")
    outfile.write("Restaurant that are 3 stars or less\n")
    for k in range(len(restname)):
        if rating[k] <= 3:
            print(restname[k],"\n")
            outfile.write(str(restname[k]) + "\n")
        k = k + 1


main()
