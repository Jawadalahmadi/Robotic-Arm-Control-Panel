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
#After creating the databases we comment out the previous command and we return to the connection phase above and we add the database's name.
#Then we go to the next step: we Create table inside of it like the following:
#mycursor.execute("CREATE TABLE motor (name VARCHAR(255), degree INTEGER(10), Status VARCHAR(255))")
#Again we comment out the table creation command. Then after creating the databases and the table we give the command to show them to us to ensure they exist. 
#(Note these two commands cant run all at once):
#mycursor.execute("SHOW DATABASES")
#mycursor.execute("SHOW TABLES")
#Then we give the print command like this:
    
for tb in mycursor:
    print(tb)




