student= {
    "name":"satyam kumar",
    "city": "mumbai",
    "age" : 23,
    "roll no": 45,
}
print(type(student))
print(student)
print(student["age"])
student["city"]= "jamui"
print(student)
student["country"]="india "
print(student)
student.pop("country")
print(student)
print(student.keys())
print(student.values())