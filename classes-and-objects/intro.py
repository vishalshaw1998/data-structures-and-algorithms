class Student:
    pass


s1 = Student()
s2 = Student()
s1.name = "Vishal"
s2.rollNumber = 12

# To get all the attributes in the object you can use __.dict__

print(s1.__dict__)

# To check if the attribute is present in the object

print(hasattr(s1, "rollNumber"))
