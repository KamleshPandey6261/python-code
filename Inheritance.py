class Parent:
    def __init__(self):
        print("Parent class Constructor")
    @classmethod
    def m1(clf):
      print("Parent class ClassMethod")
    @staticmethod
    def m2():
       print("Parentclass static method")
       
class Child(Parent):
   pass
c=Child()
c.m1()
c.m2()