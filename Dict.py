# info= {
#     "name":"Ram",
#     "id" :12,
#     "subject":["python","java","html"],
#     "topic" :("dict","set"),
#     "age":21
# }
# info["name"]="Shyam"
# info["city"]="Rewa"

# print(info)
student={
    "name":"Ram",
    "subject":{
        "hindi":55,
        "math":90
    },
    "branch":"MCA"
}
#print(student)
#print(student["subject"]["hindi"])
#print(student.get("name"))
print(student.keys())
print(student.values())
print(student.items())
new_dict={
    "name":"rahul",
    "age":32
}
student.update(new_dict)
print(student)
