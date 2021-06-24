import mysql.connector as myconnector

mydb = myconnector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="learn_python_june21",
)

select_query = "SELECT actor_id,first_name,last_name,last_update FROM Actor WHERE actor_id > %s;"
value = ('3',)

mycursor = mydb.cursor()
mycursor.execute(select_query, value)
results = mycursor.fetchall()

for eachRow in results:
    print(eachRow[1], eachRow[2])

mycursor.close()
mydb.close()