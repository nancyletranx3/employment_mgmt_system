Write an employee management system in Python that allows users to add, search, and delete employees. It should store and display five data fields about each employee, which are:

1.       Employee ID

2.       Name

3.       Department

4.       Title

5.       Salary

The program should display a menu with the following options:

1.       Add an Employee

-         If an employee with the same Employee ID already exists, then do not allow adding a new one. Having two employees with the same EID is not allowed. While adding an employee you should allow the user to either cancel the operation or re-enter the EID again.

2.       Find an Employee (By Employee ID)

-        Implement find an employee by Employee ID function. ID search should be case insensitive.

3.       Find an Employee (By Name)

-        Implement find an employee by name 

4.       Delete an Employee

-         Implement delete an employee by EID function.

5.       Display Statistics

-         Implement Display Statistics option. 
          a.       Statistics will include the number of employees in each department, as well as the total number of employees in the company.
          Hints for implementing statistics:

          Create a temporary dictionary for keeping track of departments.

          Scan all employees one by one.

          For each employee get the department name.

          Check the temporary dictionary. If the department is there, then update that entry by adding one to the value.

          If the department is not there, then create a new entry where the key equals the department name and value equals 1.

          At the end of the process, when all employees are processed, you'll have a dictionary with all departments and their employee counts.



6.       Display All Employees

-         Display all employees and their relevant information on the console.

7.       Exit

-         Exit the program.

The memory data structure that holds the information is a dictionary with employee IDs as key and the rest of the fields as a value. The data fields about each employee should also be organized into a dictionary using key/value pairs.

Your program will go through the following steps:

a)      Initialize an empty dictionary in the memory,

b)      Create a loop, display the menu, and interact with the user (each menu option will call the appropriate function corresponding that menu option,

c)       Continue displaying the menu (b) until the user selects ÂExitÂ option,

d)      Exit

Implement data persistence:

a. The program should load the data from a specific file (employee.dat) at startup and should save the data to the same file before shutdown.

b. At startup, if the file does not exist, then the program should initialize an empty dictionary in the memory and should not create a data file. If the file does exist, then it's read into a dictionary. The program should immediately close the file after reading it into memory.

c. On exit, the dictionary, empty or not, should be written to the data file. If the file already exists, the program should overwrite it, thus saving the latest state of the dictionary. The file should be immediately closed after writing into it.

d. For reading and writing a binary file, you should use pickle module described in chapter 9.

e. Your program should have a function called load() that has one string parameter containing filename and returns a dictionary unpickled from that file. If the file does not exist, then it should return an empty dictionary. The file should be closed before returning from this function.

f. Your program should have a function called save() that has two parameters, a dictionary and a filename. It should write the dictionary into this file using pickle module and close the file.
