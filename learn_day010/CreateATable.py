import mysql.connector as myconnector

mydb = myconnector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="learn_python_june21",
)

create_table_query = """
CREATE TABLE actor (
  actor_id smallint unsigned NOT NULL AUTO_INCREMENT,
  first_name varchar(45) NOT NULL,
  last_name varchar(45) NOT NULL,
  last_update timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (actor_id)
);
"""
mycursor = mydb.cursor()
mycursor.execute(create_table_query)

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

mycursor.close()
mydb.close()