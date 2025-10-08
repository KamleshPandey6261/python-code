class Employee:
    def __init__(self,name,id,state,city):
           self.name=name
           self.id=id
           self.state=state
           self.city=city
    def display(self):
          print("name = {} id = {} state = {} city = {}".format(self.name,self.id,self.state,self.city))
class Child:
      def change(emp):
         emp.id=90
         emp.state="UP"
e=Employee("Raju",11,"MP","Rewa")
e.display()
Child.change(e)
e.display()

            