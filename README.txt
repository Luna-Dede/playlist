Authors: Siraj Akmal and Andres Rivera
Project: Providing users with television show information


------------------------------Design ----------------------------------
This project utilizes object-oriented design for accessing the schema.
A televisionApp class was created for the design. An instance of the
televisionApp will connect to the "tv" schema and will have functionality
that can query and modify data.




------------------------------Libraries ----------------------------------

    Make sure to pip/conda install the following libraries:
        1. pymysql (connector to our database sql)
        2. prettytable (Allows us to tabulate data in a clean way)



------------------------Running the Program ----------------------------------
Before running this program, make sure to run the sql file dump. This will create the schema
as well as the tables necessary for the program.


The user must run this program on either the python console or
 command line. If you are using pyCharm, click on "edit
 configuration" of the main.py file and select "emulate terminal
 in output console". When you are ready, run the program.

 The program will first prompt the user with user information
 (this will allow for the connection to the tv schema). Once connected,
 a menu of options will appear. The user has the choice to view/alter
 the tables "User", "Playlist", "Episodes", "Ratings". Once a table is selected,
 the user will be shown a sub-menu with the appropriate functionality.
 A user has the ability to display, create, edit, and delete information from the
 chosen table.