# CS/IS-151 Spring 2020
# Nancy Tran
# Ch 9 HW 1

def intro():
    print("Welcome to Employee Management System (EMS)")

    main()

def main():
    db = {}
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

        user_input = int(input("Enter you selection (1..7):"))

        if (user_input == 1):
            emp_id = input("\nEnter an Employee ID or QUIT to stop:")

            if (emp_id.lower() != "quit"):
                emp_id = int(emp_id)
                db[emp_id] = {}
        
                db[emp_id]["name"] = input("\nEnter employee name:")
                db[emp_id]["dept"] = input("\nEnter employee department:")
                db[emp_id]["title"] = input("\nEnter employee title:")
                db[emp_id]["salary"] = float(input("\nEnter employee salary:\n"))
        
        elif (user_input == 2):
            find_emp_id = input("\nEnter an Employee ID or QUIT to stop:")

            while (find_emp_id.lower() != "quit"):

                get_info = db.get(find_emp_id, "\nEmployee ID: " + find_emp_id + " was not found in the database.")
                print(get_info)
                find_emp_id = input("Enter an Employee ID or QUIT to stop:\n")
        elif (user_input == 3):
            print("\nThis feature is not implemented yet.")
        elif (user_input == 4):
            delete_emp_id = input("\nEnter an Employee ID to delete or QUIT to stop:")

            if (delete_emp_id.lower() != "quit"):
                delete_emp_id = int(delete_emp_id)

                try:
                    if (delete_emp_id == emp_id):
                        del db[emp_id]
                except:
                    print("\nThis employee was not found in the database.")
            
        elif (user_input == 5):
            print("\nThis feature is not implemented yet.")
        elif (user_input == 6):
            if (len(db) != 0):
                print("\nEmployee ID:", emp_id)
                print("\tName:", db[emp_id]["name"])
                print("\tDepartment:", db[emp_id]["dept"])
                print("\tTitle:", db[emp_id]["title"])
                print("\tSalary:", format(db[emp_id]["salary"], ",.2f"))
                print("There is", len(db), "employee in the database.")
            else:
                print("\nEmployee database is empty.")
        elif (user_input == 7):
            print("\nThank you for using Employee Management System (EMS)")
            return
        else:
            print("Invalid selection. Please try again.")
            user_input = int(input("Enter you selection (1..7):"))
        
    
        
    
    
    
        
    
    
intro()
