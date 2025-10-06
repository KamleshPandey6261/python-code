a=10
def f1():
    global b
    b=100
    a=20
    print(a)
    print("Global ",globals()['a'])
f1()
print(b)