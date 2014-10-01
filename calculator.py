"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""


def main():

    keepgoing = True 

    while keepgoing == True:

        print "Hi, give us some numbers to do things with:" 
        mystring = raw_input()
        #print type(mylist)
        mystring.rstrip()
        mylist = mystring.split(' ')
        print mylist
        myoperation = mylist[0]
        num1 = mylist[1]
        num2 = mylist[2]

        if myoperation=='q':
            keepgoing=False
            print "Bye for now!"

        print myoperation, num1, num2

       
if __name__ == '__main__':
    main()