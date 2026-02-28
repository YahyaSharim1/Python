pn= input ("enter your phone number	")
if (len(pn)==10 and pn.isdigit() and pn[0]=='0'):
    print ("Valid")
else:
    print ("Invalid")