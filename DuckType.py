class Duck:
    def talk(self):
        print("This is duck.....")

class Cat:
    def talk(self):
        print("This is cat..")\
        

class Dog:
    def talk(self):
        print("This is dog...")

l=[Duck(),Cat(),Dog()]
for obj in l:
    #obj.talk()
    if hasattr(obj,"talk"):
          obj.talk()
    if hasattr(obj,"buck"):
        obj.buck();