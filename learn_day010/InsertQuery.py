import mysql.connector as myconnector

mydb = myconnector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="learn_python_june21",
)
insert_query = "INSERT INTO actor(first_name,last_name,last_update) VALUES (%s,%s,CURRENT_TIMESTAMP);"
# values = ("NIEL", "ARMSTORNG")
multiple_values = [
    ('Peter', 'Lowstreet'),
    ('Amy', 'Apple'),
    ('Hannah', 'Mountain'),
    ('Michael', 'Valley'),
    ('Sandy', 'Ocean'),
    ('Viola', 'Sideway')
]
mycursor = mydb.cursor()

# mycursor.execute(insert_one_query, values)
mycursor.executemany(insert_query, multiple_values)
mydb.commit()

print(mycursor.rowcount, " inserted into table")

mycursor.close()
mydb.close()

