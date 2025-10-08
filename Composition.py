class Car:
    def __init__(self,model,name):
          self.name=name
          self.model=model
    def display(self):
         print("name {} and model {}".format(self.name,self.model))

class Employee:
     def __init__(self,name,state,car):
          self.name=name
          self.state=state
          self.car=car
     def info(self):
          print("name {} and state {}".format(self.name, self.state))
          self.car.display()
c=Car("s11","Scaripio")
e=Employee("Ram","MP",c)
e.info()


          
        