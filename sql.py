import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",passwd="",database="user")
cr = db.cursor()

# cr.execute ('insert into user1(firstName, LastName, Email, password) values("Dhara" , "jain" , "dharajaia7655@gmail.com", "dhara@123")')
# cr.execute ('insert into user1(firstName, LastName, Email, password) values("mahima" , "singh" , "mahimasinghgmail.com", "mahima@123")')
# cr.execute ('insert into user1(firstName, LastName, Email, password) values("Garima" , "solanki" , "garimasolanki@gmail.com", "mahima@123")')
# cr.execute ('insert into user1(firstName, LastName, Email, password) values("Salman" , "Khan" , "salaman@gmail.com", "salaman@123")')



for i in range(1, 10):
    firstName = input('First Name: ')
    lastName = input('Last Name: ')
    Email = input('Email: ')
    password = input('Password: ')
    cr.execute("insert into user1 values ('%s','%s','%s','%s')"%(firstName,lastName,Email,password))
    cr.commit()

