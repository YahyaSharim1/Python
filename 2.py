num1= int (input ("tell a number"))
num2= int (input ("tell a number"))
operater= input ("choose +,*,/")
if operater == "+":
    answer= num1+num2
elif operater == "*":
    answer= num1*num2
elif operater =="/":
    answer= num1/num2
else:
    answer= None
if not (answer == None):
    print(num1,operater,num2,"=",answer)
else:
    print("Error")
    

