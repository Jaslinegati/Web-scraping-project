import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user= "Project_1",
    password= "1lovevans@!",
    database = "Proj1_db"
)

#Create a cursor object to interact with the database
cursor = mydb.cursor()

#Create a table to store the data 
cursor.execute("CREATE TABLE Goods(id INT AUTO_INCREMENT PRIMARY KEY, Title VARCHAR(255), Price FLOAT)")