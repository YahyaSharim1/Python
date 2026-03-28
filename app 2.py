file= open("Name.txt","a")


while(True):
    name= input ("Enter a name ")
    file.write("\n"+ name)
    reply=input ("Do you wish to continue Y/N  ")
    if reply =="N":
       break 
file.close()
