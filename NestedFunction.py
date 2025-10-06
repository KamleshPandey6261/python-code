def outer():
    print("This is outer function")
    def inner(a,b):
        print("This is inner function")
        return inner

f1=outer()
