class Student:
    school = "Netligent technolies: "    #  Clsss Variable 
    def __init__(self,name,mm, cm , pm):
        self.name = name
        self.mm = mm    # intance variaable :
        self.cm = cm 
        self.pm = pm 


s1=Student("Jaishankar prasad jaiswal" , 89, 67, 78)
s2=Student("Salman khan " , 99, 97, 98)
print(s1.name,s1.mm, s1.cm , s1.pm)
print(s2.name,s2.mm, s2.cm , s2.pm)

s1.mm = 89
print(s1.mm)
s2.mm= 88
print(s2.mm)
Student.school = "Coding classes"

print(Student.school)


