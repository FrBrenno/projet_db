import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="Admin123/",
    database="testdatabase"
)

mycursor = db.cursor()
