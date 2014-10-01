"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

def add(num1, num2):
    return num1+num2

def subtract(num1, num2):
    return num1-num2

def multiply(num1, num2):
    return float(num1)*float(num2)

def divide(num1, num2):
    floatnum1=float(num1)
    floatnum2=float(num2)
    return floatnum1/floatnum2

def square(num1):
    return num1**2

def cube(num1):
    return num1**3

def power(num1, num2):
    return num1**num2

def mod(num1, num2):
    return num1%num2

def main():

    print "Welcome to our calculator."
    print "It is finicky, so make sure you type with the following format:"
    print " Always use operand first (+,-,square)"
    print " To quit, press q and no spaces. Or we will mock you."

    keepgoing = True 

    while keepgoing == True:

        print "Hi, give us some numbers to do things with:" 
        mystring = raw_input()
        #print type(mylist)
        mystring.rstrip()
        mylist = mystring.split(' ')
        ##print mylist
        myoperation = mylist[0]
        
        if len(mylist) == 3: #and mylist[1].isdigit==True and mylist[2].isdigit==True
            num1 = int(mylist[1])
            num2 = int(mylist[2])

            if myoperation=='+':
                print "Your answer is: %d + %d =" % (num1, num2)
                print add(num1,num2)

            elif myoperation=='-':
                print "Your answer is: %d - %d =" % (num1, num2)
                print subtract(num1,num2)
            elif myoperation=='*':
                print "Your answer is: %d * %d =" % (num1, num2)
                print multiply(num1,num2)
            elif myoperation=='/':
                print "Your answer is: %d / %d =" % (num1, num2)
                print divide(num1,num2)

            elif myoperation=='mod': 
                print "Your remainder is:" 
                print mod(num1,num2)
            elif myoperation=='power': 
                print "Your answer is: %d ** %d =" % (num1, num2)
                print power(num1,num2) 
            else:
                print"Invalid input, try again" 

        elif len(mylist) == 2: #and mylist[1].isdigit==True
            num1 = int(mylist[1])

            if myoperation=='square':
                print "Your answer is: %d **2=" % (num1)
                print square(num1)
            elif myoperation=='cube':
                print "Your answer is: %d **3 =" % (num1)
                print cube(num1)
            else:
                print "Invalid input, try again (1)" 

        else: #myoperation.isstring()==True:
                if mylist[0]=='q':
                        keepgoing=False
                        print "Bye for now!"
                        break

                else:
                    print "Invalid input, try again (2)" 


if __name__ == '__main__':
    main()


"""
elif myoperation=='square':
    print "Your answer is: %d **2=" % (num1)
    print square(num1)
elif myoperation=='cube':
    print "Your answer is: %d **3 =" % (num1)
    print cube(num1)
"""            