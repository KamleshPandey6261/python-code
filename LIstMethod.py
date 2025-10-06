l=[10,20,30,40]
l2=[40,50,60]
print(l)
l.append(99)
print(l)
l3=l+l2
print(l3)
for x in l3:
    if x==40:
        print(x)
        break
#l3.remove(40)
#l3.pop()
l3.insert(0,00)
print(l3)
print(l3.index(20))
l3.sort()
print(l3)
l4=[x*x for x in l3 if x%2==0]
print(l4)
# packing unpacking
a=10
b=30
c=40
l=a,b,c
print(type(l))
print(min(l))
print(min(l3))