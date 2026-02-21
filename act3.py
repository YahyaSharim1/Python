count=0
un=input("Enter your username  ")
p= ("ABC123")

while (count<3):
    attempt= input("Enter your password  ")
    if p==attempt:
        print("Welcome")
    break
    
    count=count -1
    print("Die")
    