print ("Welcome all to the Student Record Program'26")
student_rec=[]
subject=[]
sub= input ("Type out the subjects(remember to use commas);  ")
subject= sub.split(",")
for i in range (len(subject)):
    subject[i]=subject[i].strip().title()
print (subject)

while(True):
    student={}
    student["Name"]=input("Enter student name ")    
    for s in subject:
        student[s]=int(input("Marks for "+s+": "))
    reply=input ("Do you wish to continue Y/N  ")
    if reply =="N":
       break 








