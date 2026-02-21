count=3

while count > 0:
    choice = input ("Choose from Vanilla, Chocolate, Strawberry  ")
    if not (choice =="Vanilla" or choice=="Chocolate" or choice=="Strawberry"):
        print("Invalid")
        continue
    count=count -1
    