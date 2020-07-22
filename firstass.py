class Emp:
    def __init__(self,eid,name,design,gmail,salary):
        self.eid=eid
        self.name=name
        self.design=design
        self.gmail=gmail
        self.salary=salary
    def printvalue(self):
        print("eid",self.eid,"name",self.name,"design",self.design,"gmail ",self.gmail,"salary ",self.salary)
f=open("C:/Users/pranav/PycharmProjects/firstproject/database/employee")
emp=[]
for data in f:
    empl=data.rstrip("\n").split(",")
    print(empl)
    eid=empl[0]
    name=empl[1]
    design=empl[2]
    gmail=empl[3]
    salary=empl[4]
    ob=Emp(eid,name,design,gmail,salary)
    emp.append(ob)
for empl in emp:
    salary=empl.salary
    print(max(salary))