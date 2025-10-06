from functools import reduce
# a=lambda a,b,c:a+b+c
# print(a(10,20,30))

# b=lambda a,b: a if a>b else b
# print(b(20,30))
# filter ()
l=[10,11,12,13,14,15,16]
#l1=list(filter(lambda x:x%2==0,l))
#print(l1)
#l1=list(filter(lambda x:x>15,l))
#print(l1)

l1=[10,20,30,40]
# l2=list(map(lambda x:x+x, l1))
# l3=list(map(lambda x:x*x, l1))
# print(l2)
# print(l3)
# 
re=reduce(lambda x,y:x+y,l1)
print(re)

