class Race:
    def run1(a):
        print("Run1 is calling: ")
    def run2(a):
        print("Run2 is calling: ")

class Race2:
    def run3(a):
        print("Run3 is calling: ")
    def run4(a):
        print("Run4 is calling : ")

obj1 = Race()
obj1.run1()
obj1.run2()

obj2 = Race2()
obj2.run3()
obj2.run4()