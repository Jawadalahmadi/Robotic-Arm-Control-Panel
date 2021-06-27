# Robotic-Arm-Control-Panel
I started on a project of creating a robotic arm and controlling it online. On the controlling and programming side of things i decided to choose Python as my programming language for this task and MySQL to create my database. 
I started with the UI first then created the database and after that i connected the two together which i will explain below.

# User-Interface
I started by importing the tkinter library in Python to create and customize my UI. I first created my window and chose the title, the size and the color. 
Then i started on creating the six sliders i will be using in this UI while also choosing their colors and sizes and also their place on the UI, while also assigning a label which contains the sliders name on its left side. I repeated this step for each slider until they were all prepared and ready
Then i added the buttons "Save" and "Run" but currently they have no function, this will be added later when i connect it to the database.
Due to the limitations of python programming i couldn’t customize my UI in an fashionable way so the UI we created is basic.

# Database
I first started creating my database by launching MySQL and creating a server inside of it. Then i connected mySQL using the mysql.connector function and defined the host, username and password.
After that i created my database after defining the connection with MySQL as mycursor and i named the database robotdb. I then commented the creation command and went back to the connection and added the database and its name there. I added a command to show me the database to ensure its existence after that I commented the command so it won’t overlap
So now mycursor also has the database defined in it and we can create a table and place it inside the database which we did and named the table motor and added 3 columns inside of it "name", "degree", "Status". lastly in order to ensure out work is complete i gave the "SHOW TABLES" Command to ensure the table was correctly created.
"NOTE: because i took the picture after i finished all three subtasks i had to include the array from the next task in the picture that was uploaded within the database file as i couldnt return the database's table to it orignal form after creation without some complications.

# Connecting UI to DB
Now time to connect them both. I went back to the User interface code and added 2 new functions, The first was called Values which contains an array that will take the values of the sliders and store them in the database according to their names, i also connected the database using the same method in the Database code, this function will only run if the "Save" button was pressed.
The second function was added to the "Run" button command which will turn the default "OFF" status for each slider to "ON" upon being clicked.
I uploaded a picture that shows the changed values of the database after running the code.
