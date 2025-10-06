s="aabbccjjamdd"
d={}
for key in s:
    d[key]= d.get(key,0)+1
for k,v  in d.items():
    print(k,v)