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

-        Not functional in phase 1. This function will only display a message that this option is not functional yet and will be implemented soon.

4.       Delete an Employee

-         Implement delete an employee by EID function.

5.       Display Statistics

-         Not functional in phase 1. This function will only display a message that this option is not functional yet and will be implemented soon.

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
