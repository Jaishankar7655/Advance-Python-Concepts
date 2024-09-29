# Abstarion  

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def Show():
     pass
    
class Circle(Shape):
    def Show(self):
        print("circle has no edeges:...")

class square(Shape):
    def  Show(self):
        print("Square have four side....")

obj1 = square()
obj1.Show()

import abc
print(dir(abc))
        
