# CS/IS-151 Spring 2020
# Nancy Tran
# Phase 3

class Employee:
    def __init__(self, emp_id, name, dept, title, salary):
        self.__emp_id = emp_id
        self.__name = name
        self.__dept = dept
        self.__title = title
        self.__salary = salary

    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    def set_name(self, name):
        self.__name = name

    def set_dept(self, dept):
        self.__dept = dept

    def set_title(self, title):
        self.__title = title

    def set_salary(self, salary):
        self.__salary = salary

    def get_emp_id(self):
        return self.__emp_id

    def get_name(self):
        return self.__name

    def get_dept(self):
        return self.__dept

    def get_title(self):
        return self.__title

    def get_salary(self):
        return self.__salary

    def __str__(self):
        return "Employee ID: " + str(self.__emp_id) + "\n" + \
               "\tName: " + self.__name + "\n" + \
               "\tDepartment: " + self.__dept + "\n" + \
               "\tTitle: " + self.__title + "\n" + \
               "\tSalary: " + str(self.__salary)

import pickle as p

FILENAME = 'employee.dat'

def main():
    intro()

    db = load()

    exit = False

    while not exit:
        print("Main Menu:")
        print("1.	Add an Employee")
        print("2.	Find an Employee (By Employee ID)")
        print("3.	Find an Employee (By Name)")
        print("4.	Delete an Employee")
        print("5.	Display Statistics")
        print("6.	Display All Employees")
        print("7.	Exit")

        selection = False
        while not selection:
            user_input = input("Enter you selection (1..7):\n")

            if (user_input == '1'):
                emp_id = input("Enter an Employee ID or QUIT to stop:")

                if (emp_id.lower() != "quit"):
                    emp_id = int(emp_id)
                    if (emp_id in db):
                        print("This employee ID has already been taken. Please try again.")
                        pass
                    else:
                        name = input("\nEnter employee name:")
                        dept = input("\nEnter employee department:")
                        title = input("\nEnter employee title:")
                        salary = float(input("\nEnter employee salary:\n"))

                        entry = Employee(emp_id, name, dept, title, salary)
                        db[emp_id] = entry
                        selection = True
            
            elif (user_input == '2'):
                emp_id = input("Enter an Employee ID or QUIT to stop:")

                if (emp_id.lower() != "quit"):
                    emp_id = int(emp_id)
                    if (emp_id in db):
                        print(db.get(emp_id, "Not found"))
                        selection = True
                    else:
                        print("Employee ID: " + str(emp_id) + " was not found in the database.")
                        selection = True
                    
                        emp_id = input("Enter an Employee ID or QUIT to stop:\n")
                        
            elif (user_input == '3'):
                name = input("Enter an employee name or QUIT to stop:")
                
                if (name.lower() != "quit"):
                    for key, value in db.items():
                        if (value.get_name() == name):
                            new_emp_id = key
                            print(db.get(new_emp_id, "Employee Name: " + name + " was not found in the database."))
                            selection = True
                    
                    
            elif (user_input == '4'):
                emp_id = input("Enter an Employee ID to delete or QUIT to stop:")

                if (emp_id.lower() != "quit"):
                    emp_id = int(emp_id)

                    try:
                        if emp_id in db:
                            del db[emp_id]
                    except:
                        print("This employee was not found in the database.")
                
            elif (user_input == '5'):
                departments = {}

                num_dept = 0
                count = "Employee Count"
                total_salary = "Total Salary"
                min_salary = "Minimum Salary"
                max_salary = "Maximum Salary"

                for key, value in db.items():
                    depts = value.get_dept()
                    salary = value.get_salary()
                    db_count = departments.get(depts, {}).get(count)

                    if (depts in departments):
                        
                        db_count += 1
                        departments[depts][count] = db_count

                        db_salary = departments.get(depts, {}).get(total_salary)
                        db_salary = db_salary + salary
                        departments[depts][total_salary] = db_salary

                        db_min_salary = departments.get(depts, {}).get(min_salary)
                        db_max_salary = departments.get(depts, {}).get(max_salary)

                        if (db_min_salary > salary):
                            departments[depts][min_salary] = salary

                        elif (db_max_salary < salary):
                            departments[depts][max_salary] = salary

                    else:
                        db_count = 1
                        stats = {count : db_count, total_salary : salary, \
                                       min_salary : salary, max_salary : salary}
                        departments[depts] = stats
                        num_dept += 1

                if (len(departments) == 0):
                    print("There are no departments in the database.")
                    print("Employee database is empty.")
                    selection = True

                else:
                    print("Department Statistics:")

                    for key, value in sorted(departments.items()):
                        if (value[count] == 1):
                            print("\tDepartment:", key, "-", value[count], "employee")
                            print("\t\tMaximum Salary: $", format(value[max_salary], ",.2f"))
                            print("\t\tMinimum Salary: $", format(value[min_salary], ",.2f"))
                            print("\t\tAverage Salary: $", format(value[total_salary]/value[count], ",.2f"))
                                                        
                        else:
                            print("\tDepartment:", key, "-", value[count], "employees")
                            print("\t\tMaximum Salary: $", format(value[max_salary], ",.2f"))
                            print("\t\tMinimum Salary: $", format(value[min_salary], ",.2f"))
                            print("\t\tAverage Salary: $", format(value[total_salary]/value[count], ",.2f"))
                            
                    if (len(departments) == 1):
                        print("There is", len(departments), "department in the database.")
                        print("There is", len(db), "employee in the database.")
                        selection = True

                    elif (len(departments) > 1):
                        print("There are", len(departments), "departments in the database.")
                        print("There are", len(db), "employees in the database.")                    
                        selection = True

                
            elif (user_input == '6'):
                if (len(db) == 0):
                    print("Employee database is empty.")
                    
                    selection = True
                else:
                    for empid, stat in db.items():
                        print(stat)

                    if (len(db) == 1):
                        print("There is", len(db), "employee in the database.")
                    elif (len(db) > 1):
                        print("There are", len(db), "employees in the database.")
                    
                    selection = True
                    
            elif (user_input == '7'):
                print("Thank you for using Employee Management System (EMS)")
                save(db)
                return
            else:
                print("Invalid selection.")
                continue
    
            save(db)

def intro():
    print("Welcome to Employee Management System (EMS)")
    

def load():
    try:
        input_file = open(FILENAME, 'rb')

        db = p.load(input_file)

        input_file.close()
    
    except:
        print("Unable to load the database from binary file " + FILENAME + ".")
        print("Creating an empty database.")

        db = {}
        
    return db

def save(db):
    output_file = open(FILENAME, 'wb')

    p.dump(db, output_file)


    output_file.close()


main()

