import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="admin",
)

mycursor = db.cursor()
