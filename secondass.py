import re
g='[a-zA-z]\w*@gmail.com'
f=open("C:/Users/pranav/PycharmProjects/firstproject/work2/mail")
for data in f:
    rec=data.rstrip("\n")
    match=re.fullmatch(g,rec)
    if(match!=None):
        f2=open("valid","a")
        f2.write(rec)
        f2.write("\n")
    else:
        print("invalid variable name")