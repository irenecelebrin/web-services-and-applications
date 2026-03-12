## lab 6.2 Create python code to connect database to server
# author: irene celebrin
# date: 2026-03-12

# create a table using python code 
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="wsaa"
)

mycursor = connection.cursor()
sql = "CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)"
mycursor.execute(sql)

mycursor.close()
connection.close()

