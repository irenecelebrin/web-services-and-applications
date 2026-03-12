## lab 6.2 Create python code to connect database to server
# author: irene celebrin
# date: 2026-03-12

# create a database using python code 
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)

mycursor = connection.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS wsaa")
mycursor.close()
connection.close()

