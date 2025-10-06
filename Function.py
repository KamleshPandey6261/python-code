def square(n):
    return n*n
print(square(10))
def display(name="Ram"):
    print("MY name is ",name)
display("Shyam")

#Keyword argumnt 
def  msg(sal,name="Raju",age=20):
     print("My name is ",name,"And age is ",age,"ans sal is ",sal )


msg("KK")
# variable parameter
def  f1(*n):
    sum=0
    for x in n:
        sum=sum+x
    print(sum) 
f1(10)
f1(10,20)
f1(10,20,30)
f1(10,20,30,40)