import mysql.connector 
cr = mysql.connector.connect(host="localhost", user="root", passwd="", database="user")
db = cr.cursor()
cr.execute("create table user2 (username varchar(100) , password varchar(100) , email varchar(100)")
print ("press 1 for  Login ")
print ("Press 2 enter to regitration")


def regitration():
    FirstName = input("enter your name: ")
    lastName = input("enter your last name: ")
    password = input("enter your password: ")
    Email=input("enter your email: ")
    cr.execute("insert into user2 values (%s, %s, %s, %s)" % (FirstName, lastName, Email, password))
    cr.commit()
    print("Restration succesfuly completed")

def login():
    Email = input("enter your email")
    Password = input("enter your password: ")
    cr.execute("select * from user2 ")
    r = cr.fetchone()
    if Email==r[4] and Password==r[3]:
        print("login successful")
    else:
        print("login failed")

n= int(input("enter choice :"))
if n==1:
    login()
elif n==2:
    regitration()

else:
    print("enter invalid choice :")






       