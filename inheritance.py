
# single inhertance 
'''
class Parents:
    def base(self):
        print("hello jaishankar prasad jaiswal")
class Parents2(Parents):
        def Base2(self):
         print("hello one is printing")
obj = Parents2()
obj.Base2()
obj.base()

'''

# multilevel inheritance :

'''
class Base1:
    def feature1(self):
        print("Base 1 class is running: ")

class Base2(Base1):
     def feature2(self):
        print("Base 2 class is running: ")

class Base3(Base2):
     def feature3(self):
        print("Base 3 class is running: ")

class Base4(Base3):
     def feature4(self):
        print("Base 4 class is running: ")

obj = Base4()
obj.feature1()
obj.feature2()
obj.feature3()
obj.feature4()
'''

# multiple inheritance
'''
class Parent:
    def Function1(self):
        print("line one is printing: ")
class Base1:
    def Function2(self):
        print("line Two is printing: ")
class Base2:
    def Function3(self):
        print("line Three is printing: ")
class Base3(Parent,Base1, Base2):
    def Function4(self):
        print("line Two is printing: ")
obj = Base3()
obj.Function1()
obj.Function2()
obj.Function3()
obj.Function4()

'''







