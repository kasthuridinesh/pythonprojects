import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="Atmecs@123")

mycursor = mydb.cursor()

mycursor.execute("CREATE SCHEMA `EMS`")
print("success create database")
