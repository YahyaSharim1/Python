num1= int (input ("tell a number"))
num2= int (input ("tell a number"))
operater= input ("choose +,*,/")
if operater == "+":
    answer= num1+num2
    print (answer)
else:
    if operater == "*":
        answer= num1*num2
        print (answer)
    else:
       if operater == "/":
           answer= num1/num2
           print (answer)
       else:
           print ("Incorrect")
         
