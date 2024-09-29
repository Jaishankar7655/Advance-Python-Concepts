from functools import reduce

def subtract(a, b):
    return a - b
while True:
   print("Select your option: ")
   print("1 for Addition: ")
   print("2 for Multiplication: ")
   print("3 for Subtraction: ")
   print("4 for Division: ")
   option = int(input("Select operation: "))

# code for Addition  

   class Addition:
     def Sum(self):
      n = int(input("Enter your Range: "))
      list = []
      number = 1
      for i in range(1, n+1):
         num = int(input("Enter Number: "))
         list.append(num)
      for i in list:
         number = number+i
      print("Your Addition of" ,list,"is",  number)


# code for mutliplication:
   class Multiplication:
     def mul(self):
      n = int(input("Enter your Range: "))
      list = []
      number = 1
      for i in range(1, n+1):
         num = int(input("Enter Number: "))
         list.append(num)
      for i in list:
         number = number+i
      print("Your Addition of" ,list,"is",  number)



# code for Subtraction:

     class Subtraction:
        def subs(self):
            n = int(input("Enter your Range: "))
            numbers = []
            for i in range(1, n+1):
                v = int(input("Enter A number: "))
                numbers.append(v)
            result = reduce(subtract, numbers)
            print("Your Subtraction of", numbers, "is", result)

# code for division 
     class division:
         def div(self):
          n = int(input("Enter your Range: "))
          list = []
          number = 1
          for i in range(1, n+1):
               num = int(input("Enter Number: "))
               list.append(num)
          for i in list:
            number = number/i
          print("Your Addition of" ,list,"is",  number)



     if option ==1:
        obj = Addition()
        obj.Sum()
     elif option ==2:
        obj = Multiplication()
        obj.mul()
     elif option ==3:
        obj = Subtraction()
        obj.subs()
     elif option ==4:
        obj = division()
        obj.div()
     else:
        print("Please Select a valid option: ")

        




