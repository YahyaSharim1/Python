reply=True
while reply:
    n1= input("enter")
    n2= input("enter")
    total=n1+n2
    print(total)
    re= input("Do you wish to continue,Y/N")
    if re.upper=="y":
        reply=True
    else:
        reply=False
        
    