class Sum:
    def __init__(self, n , m):
        self.n = n
        self.m = m
    def sm(self):
        print("sum of the number is ", self.n + self.m)
        
class Subtration:
    def __init__(self, n , m):
        self.n = n
        self.m = m
    def sb(self):
        print("sum of the number is ", self.n - self.m)
        
class Multiplication:
    def __init__(self, n , m):
        self.n = n
        self.m = m
    def ml(self):
        print("sum of the number is ", self.n * self.m)
        
class Division:
    def __init__(self, n , m):
        self.n = n
        self.m = m
    def dv(self):
        print("sum of the number is ", self.n / self.m)
print("1 for addition: ")
print("2 subtartion:  ")
print("3 for Division: ")
print("4 for multiplication: ")
while True:
    number = int(input("selct your choice: "))
    n = int(input("Enter your number: "))
    m = int(input("Enter your number: "))
    if number ==1:
        obj1 = Sum(n, m)
        obj1.sm()
    elif number ==2:
        obj1 = Subtration(n, m)
        obj1.sb()
    elif number ==3:
        obj1 = Multiplication(n, m)
        obj1.ml()
    elif number ==4:
         obj1 = Division(n, m)
         obj1.dv()
    else:
         print("select you right choices: ")
