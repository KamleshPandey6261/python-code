a=10
class Student:
    print(a)   
    print(a)
    def __init__(self,id,name,age,roll,branch):
        self.id=id
        self.name=name
        self.age=age
        self.roll=roll
        self.branch=branch
    def dicplay(self):
    
        a=22
        print("After chanded a is ",a)
        print("id = {} name = {} age={} roll = {} and branch ={} ".format(self.id,self.name,self.age,self.roll, self.branch))
s1=Student(10,"Ram",21,"ABC1234","MCA")
s2=Student(10,"Shyam",20,"ABC1234334","MCA")
s1.dicplay()
#s2.dicplay()
print(a)

