count=3
password= ("ABC123")
while count>0:
    un= input ("What is your name")
    attempt= input("Enter your password  ")
    if password==attempt:
        print("Welcome")
        break
    
    count=count -1
    print("Die")