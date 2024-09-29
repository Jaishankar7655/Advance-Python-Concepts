class Student:
    school = "Netligent technolies: "    #  Clsss Variable 
    def __init__(self,name,mm, cm , pm):
        self.name = name
        self.mm = mm    # intance variaable :
        self.cm = cm 
        self.pm = pm 
    def total(self):
        total = print("Total marks is: " ,self.mm +self.cm +self.pm)
        print(total)
    def avg(self):
         per = print("Total '%' is: " ,(self.mm +self.cm +self.pm)//3)
         print(per) 
    @classmethod
    def sch(cls):
        print(cls.school)
    @staticmethod
    def intro():
        print("Hello every one this is python class")
s1=Student("Jaishankar prasad jaiswal" , 89, 67, 78)
s2=Student("Salman khan " , 99, 97, 98)

s1.total()
s1.avg()
s1.sch()
s1.intro()



