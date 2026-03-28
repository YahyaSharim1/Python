lis=[]
file= open("Name.txt","r")

for line in file:
    lis.append(line.strip())
print (lis)
    
ind= int (input ("Choose an index to edit "))
name=input ("Name ")
lis[ind-1]= name
print (lis)


