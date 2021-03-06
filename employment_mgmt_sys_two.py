# CS/IS-151 Spring 2020
# Nancy Tran
# Phase 2

import pickle as p

def main():
    intro()

    file_name = 'employee.dat'

    db = load(file_name)

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
                        db[emp_id] = {}
                
                        db[emp_id]["name"] = input("\nEnter employee name:")
                        db[emp_id]["dept"] = input("\nEnter employee department:")
                        db[emp_id]["title"] = input("\nEnter employee title:")
                        db[emp_id]["salary"] = float(input("\nEnter employee salary:\n"))
                        selection = True
            
            elif (user_input == '2'):
                emp_id = input("Enter an Employee ID or QUIT to stop:")

                if (emp_id.lower() != "quit"):
                    emp_id = int(emp_id)
                    if (emp_id in db):
                        print("\nEmployee ID:", emp_id)
                        print("\tName:", db[emp_id]["name"])
                        print("\tDepartment:", db[emp_id]["dept"])
                        print("\tTitle:", db[emp_id]["title"])
                        print("\tSalary:", format(db[emp_id]["salary"], ",.2f"))
                        selection = True
                    else:
                        print("Employee ID: " + emp_id + " was not found in the database.")
                        selection = True
                    
                        emp_id = input("Enter an Employee ID or QUIT to stop:\n")
            elif (user_input == '3'):
                emp_name = input("Enter an employee name or QUIT to stop:")

                count = 0
                if (emp_name.lower() != "quit"):
                    for key, value in db.items():
                        if (emp_name in value["name"]):
                            count =+ 1
                            print("\nFound", count, "employee with that name.")
                            print("Employee ID:", key)
                            print("\tName:", value["name"])
                            print("\tDepartment:", value["dept"])
                            print("\tTitle:", value["title"])
                            print("\tSalary:", format(value["salary"], ",.2f"))
                            selection = True
                        else:
                            print("Employee Name: " + emp_name + " was not found in the database.")
                    
                    
                    
            elif (user_input == '4'):
                delete_emp_id = input("Enter an Employee ID to delete or QUIT to stop:")

                if (delete_emp_id.lower() != "quit"):
                    delete_emp_id = int(delete_emp_id)

                    try:
                        if (delete_emp_id == emp_id):
                            del db[emp_id]
                    except:
                        print("This employee was not found in the database.")
                
            elif (user_input == '5'):
                print("Department Statistics:")

                departments = {"Engineering": 0}

                for empid, stats in db.items():
                    if (stats["dept"] in departments):
                        departments[stats["dept"]] += 1
                    else:
                        departments[stats["dept"]] = 1

                for stats, values in departments.items():
                    if (values == 1):
                        print("\tDepartment:", stats, "-", values, "employee")
                        print("There is", len(departments), "department in the database.")
                        print("There is", len(db), "employee in the database.")
                        selection = True

                    else:
                        print("\tDepartment:", stats, "-", values, "employees")

                
                if (len(departments) > 1):
                    print("There are", len(departments), "departments in the database.")
                    print("There are", len(db), "employees in the database.")
                    
                    
                    selection = True
                
            elif (user_input == '6'):
                if (len(db) != 0):
                    for empid, stat in db.items():
                        print("Employee ID:", empid)
                        print("\tName:", db[empid]["name"])
                        print("\tDepartment:", db[empid]["dept"])
                        print("\tTitle:", db[empid]["title"])
                        print("\tSalary:", format(db[empid]["salary"], ",.2f"))

                    if (len(db) == 1):
                        print("There is", len(db), "employee in the database.")
                    else:
                        print("There are", len(db), "employees in the database.")
                    selection = True
                else:
                    print("Employee database is empty.")
                    selection = True
                    
            elif (user_input == '7'):
                print("Thank you for using Employee Management System (EMS)")
                return
            else:
                print("Invalid selection.")
                continue

                
            
        

    save(db, file_name)

def intro():
    print("Welcome to Employee Management System (EMS)")
    

def load(file_name):
    try:
        input_file = open(file_name, 'rb')
        db = p.load(input_file)
        input_file.close()
    
    except:
        print("Unable to load the database from binary file " + file_name + ".")
        print("Creating an empty database.")

        db = {}
        
    return db

def save(db, file_name):
    output_file = open(file_name, 'wb')

    p.dump(db, output_file)


    output_file.close()

    return db, output_file

    menu(db)

main()

