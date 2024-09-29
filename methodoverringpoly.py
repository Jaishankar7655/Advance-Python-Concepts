# Polymorphism 
     # 1. method overiding 
     # 2. method overloading 

class Student:
    def marks(self , a=None, b = None , c=None , d= None):
        if a!=None and b!=None and c==None and d==None:
            return(a+b)
        elif a!=None and b!=None and c!=None and d==None:
            return(a+b+c)
        elif a!=None and b!=None and c!=None and d!=None:
            return(a+b+c+d)
        elif a!=None and b==None and c==None and d==None:
            return(a+b+c+d)
        elif a==None and b==None and c==None and d==None:
            return("sorry , null value")
obj =  Student()
print(obj.marks())
print(obj.marks(1,2))
print(obj.marks(1,2,3))
print(obj.marks(1,2,3,4))

