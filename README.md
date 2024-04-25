# Project for CMPSC 431W
Setup
----------------------
**1. Installation**
- You must have Python and SQLite installed on your desktop
- Clone or download the repository into your desired directory

**2. Initialization** 
Open your terminal window, navigate to the directory where your .sql and .py files are located, and run these commands: 
```
$ sqlite3
$ DogBreed.db
$ .read DogBreed.sql
```
This will create your DogBreed.db from your .sql file.

**3. Running the CLI User Interface**
Open a new terminal. This will be the terminal for your CLI interface. Run this command.
```
$ python3 DogBreedUI.py
```
You will be met with the CLI interface window. 

CLI Interface
-------------
You will see 12 options on the CLI interface window

**Option 1 (Insert Data):** Add new records of a dog breed to your table of choice

**Option 2 (Delete Data):** Remove records of a dog breed from a table of choice

**Option 3 (Update Data):** Modify records of a dog breed in the table of your choice

**Option 4 (Search Data):** Search for records of dog breeds based on specific criteria

**Option 5 (Aggregate Functions):** Implement functions (sum, average, max, etc) onto the data

**Option 6 (Sorting):** Arranging query results based on specific criteria

**Option 7 (Joins):** Combined data from multiple tables

**Option 8 (Grouping):** Grouped query results based on specific criteria

**Option 9 (Subqueries):** Nested operations within queries

**Option 10 (Transactions):** Ensured consistency within database operations

**Option 11 (Error Handling):** Throws an error when there is an exception in database operations

**Option 12 (Exit):** Exit the interface

Enter the desired number into the input. From there, each option will prompt you with instructions to input desired records, operations, or criteria. Please follow them for a successful operation. Some options will ask you to choose a table to do the desired database operations in. Other options will simply ask to input the desired functions, order, and other operations.

**Have fun!**
