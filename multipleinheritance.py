'''
class Square:
     def __init__(self ,a):
          self.a = a
     def sq(self):
          print(self.a*self.a)
          
          
class Cube:
     def __init__(self, a):
          self.a = a
     def cb(self):
           print(self.a*self.a*self.a)

class Factorial():
     def __init__(self , a):
          self.a = a
     def fc(self):
          f = 1
          for i in range (1, self.a+1):
               f= f*i;
          print(f) 

class User(Square, Cube, Factorial):
     pass
obj = User(4)
obj.sq()
obj.cb()
obj.fc()


'''



'''
class Square:
     def __init__(self ,a):
          self.a = a
     def sq(self):
          print(self.a*self.a)
              
class Cube(Square):
     def __init__(self, a):
          self.a = a
     def cb(self):
           print(self.a*self.a*self.a)

class Factorial(Cube):
     def __init__(self , a):
          self.a = a
     def fc(self):
          f = 1
          for i in range (1, self.a+1):
               f= f*i;
          print(f) 

class User(Factorial):
     pass
obj = User(4)
obj.sq()
obj.cb()
obj.fc()


'''


class Square:
     def __init__(self ,a):
          self.a = a
     def sq(self):
          print(self.a*self.a)
              
class Cube:
     def __init__(self, a):
          self.a = a
     def cb(self):
           print(self.a*self.a*self.a)

class Factorial(Cube):
     def __init__(self , a):
          self.a = a
     def fc(self):
          f = 1
          for i in range (1, self.a+1):
            f = f*i;
          return (f)

class User(Factorial , Square):
     pass
n = int(input("enter a number: "))
obj = User(n)
obj.sq()
obj.cb()
print(obj.fc())






