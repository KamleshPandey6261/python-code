class Student:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!= None and c!=None:
            print("The Sum is ",a+b+c)
        elif a!=None and b!=None :
            print("The sum is ",a+b)
        elif a!=None:
            print ("THE sum is ",a)
s=Student()
s.sum(10,20,30)
s.sum(10,20)
s.sum()

