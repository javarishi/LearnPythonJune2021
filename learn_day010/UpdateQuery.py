import mysql.connector as myconnector

mydb = myconnector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="learn_python_june21",
)

update_query = "UPDATE actor SET first_name = %s, last_name = %s, last_update = CURRENT_TIMESTAMP WHERE actor_id = %s;"
values = ("NEIL", "ARMSTORNG", "1")
mycursor = mydb.cursor()
mycursor.execute(update_query, values)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

mycursor.close()
mydb.close()