#dictionary
student = {"name":"Fatima", "age": 10, "grade": 5}
print(student)
print("my name is", student["name"])
print("i am ",student["age"],"years old")
print("i am in grade",student["grade"])
student["country"] = "China"
student["hobby"] = "skating"
print(student)
del student["country"]
print(student)
print(len(student))
student.clear()
print(student)
#country code
country_code = {"China" : 86, "India" : 91, "Pakistan" : 92}
print(country_code.get("Pakistan", "not found"))
print(country_code.get("Nepal", "not found"))