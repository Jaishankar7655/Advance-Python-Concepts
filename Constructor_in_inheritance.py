'''method resultion order :
class A:
    def __init__(self):
        print("Class A is Running....")
class B:
    def __init__(self):
        print("Class b is Running....")
class C(A, B):
    def features(self):
        super().__init__()
        super().__init__()
        print("Class B is running....")
obj = B()
'''



# Counstructor in inheritane: 


class A:
    def __init__(self):
        print("Class A is Running....")
class B(A):
    def features(self):
        print("Class B is running")
class C(B):
    def __inint__(self):
        super.__init__()
        super.__init__()
        print("Class c is running: ")
obj = C()
