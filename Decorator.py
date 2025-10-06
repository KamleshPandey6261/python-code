
def dc(func):
      def inner(name):
             if(name=="Kalu"):
                print("Hello ",name," Bad morning")
             else:
              func(name)
      return inner

@dc
def message(name):
    print("Hello sunnay ",name," Good morning")
message("Ram")