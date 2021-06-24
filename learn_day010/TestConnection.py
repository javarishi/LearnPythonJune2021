import mysql.connector as myconnector

mydb = myconnector.connect(
    host="localhost",
    user="root",
    passwd="password"
)
'''
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE learn_python_june21")
mycursor.close()
'''
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

for eachDatabase in mycursor:
    print(eachDatabase)

mycursor.close()
print("Connection is created, database is created")
mydb.close()
