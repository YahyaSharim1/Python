#num1=[1,2,3,4,5]
#num2=[6,7,8]
#fin=[]
#for num in num1:
  #  fin.append(num)
#for num in num2:
  #  fin.append(num)
    
#print (fin)

#num3=[20,25,30,35,40]
#num4=[30,12,25,14,35]
#com=[]

#for num in num3:
  #  for n in num4:
    #     if n==num:
    #         com.append(n)
         
      
#print (num)
    
num5=[1,2,3,4,5,6,7,8,9]
even=[]
odd=[]

for num in num5:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)

print (even)
print (odd)


info={'name':'Yahya','age':15}

print (info)
print('My name is',info['name'])

#info2={'name':Yahya,'age':15,'city':Tokyo}

name= input ("Your name pls ")
age= input ("your age pls ")
city= input ("your city pls ")
friend={}
friend['name']=name
friend['age']=age
friend['city']=city
print(friend)
