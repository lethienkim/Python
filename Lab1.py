Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # program to compute the Amount paid to the movie company
>>> #
>>> #
>>> #name: Thienkim Le
>>> #COSC 1336 Fundamentals of Programming
>>> #ACC SPRING 2003
>>> #lab1.py
>>> #Professor Onabajo
>>> #Golbal variable
>>> percent= .20
>>> def main():
...         #variabale declaration
...         child_t=3.00
...         adult_t=6.00
...         aticket_sold=0
...         cticket_sold=0
...         gross=0.0
...         net=0.0
...         amount_paid=0.0
...         movie_name="  "
...         #promt user for input
...         movie_name=input("Please ente Movie Name   ")
...         aticket_sold=int(input(Please enter adult ticket sold   "))
...                                
SyntaxError: unterminated string literal (detected at line 13)
>>> def main():
...         #variabale declaration
...         child_t=3.00
...         adult_t=6.00
...         aticket_sold=0
...         cticket_sold=0
        gross=0.0
        net=0.0
        amount_paid=0.0
        movie_name="  "
        #promt user for input
        movie_name=input("Please ente Movie Name   ")
        aticket_sold=int(input("Please enter adult ticket sold   "))
        cticket_sold=int(input("Plese enter child ticket sold  "))
        #compute
        gross=child_t*cticket_sold + cadult-t*aticket_sold
        net=gross*percent
        amount_paid=gross-net
        #outout
        print("Movie Name  ",movie_name)
        print("Adult ticket sold",aticke_sold)
        print("Child ticket sold",cticket_sold)
        print("Gross ",gross)
        print("Net",net)
        print("Amount paid to movie company  ",amount_paid)
        #hold screen
        dummy=input("please press anykey to continue")
