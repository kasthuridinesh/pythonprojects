# *************************CREATE NEW DATABASE and SHOW DATABASE******************
import mysql.connector
# Creating data base
myconnect = mysql.connector.connect(host='localhost', user='root', password='Atmecs@123')

print(myconnect)
# Printing data's in the database
mycursor = myconnect.cursor()

mycursor.execute("CREATE SCHEMA `kasthuri`")

mycursor.execute("SHOW SCHEMAS")
for db in mycursor:
    print(db)
# creating customer table

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Atmecs@123",
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
