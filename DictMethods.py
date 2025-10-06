d={
    "id":10,
    "name":"Ram",
    "age" : 20
}
#print(d)
# travers
for k,v in d.items():
    print(k,end=" ")
    print(v)
#print(d.keys())
#print(d.values())
print(d)
d["name"]="Hari"
print(d)
print(d["name"])

print(d.get("Hari"))
print(d.get("Hari","Hari Narayam"))