# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()

name = "Isiah Alinab"
age = 19
gpa = 1.96
is_student = True

print(type(name))#The type variable works as a identifer of what type it is.
#Converting a data into something else
gpa = int(gpa)
print(gpa)
#And apparently we can also do this shet too
age = (str(age))
age += "1"
print(age)
#Boolean still works as is but as long as there is value, its true
gpa = bool(gpa)
print(gpa)