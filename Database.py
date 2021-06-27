import mysql.connector 
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass123",
    #We add the next part after creating the database 
    #database="robotdb"  
    )


mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE robotdb")
#After creating the databases we Create table inside of it like the following:
#mycursor.execute("CREATE TABLE motor (name VARCHAR(255), degree INTEGER(10), Status VARCHAR(255))")
#After creating the databases and the table we gove the command to show them to us to ensure they exist:
#mycursor.execute("SHOW DATABASES")
#mycursor.execute("SHOW TABLES")
#Then we give the print command like this:
    
for tb in mycursor:
    print(tb)




