import mysql.connector
db = mysql.connector.connect(host = "localhost", user="root", passwd="", database="user")
cr = db.cursor()

print("press 1 for login: ")
print("press 2 for registration: ")

n = int(input("selct options according to your choices: "))
if n==1:
    FN = input("enter your first name:")
    LN = input("enter your Last name:")
    EM = input("enter your email: ")
    PS= input("enter password: ")
    cr.execute('insert into user1 values("%s","%s","%s","%s")' %(FN, LN, EM ,PS))
    db.commit()
    print("registration succesfull")
elif n==2:
    EM = input("enter your email: ")
    PS= input("enter password: ")
    cr.execute("select * from user1")
    r = cr.fetchone()
    # print(r)
    if EM==r[2] and PS==r[4]:
        print("Login succesfully: ")
    else:
        print("Login incorrect: ")
else:
    print("Enter Valid Options: ")


