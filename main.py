# check for valid email
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Check if employee information is invalid
isInvalid = True

# Employee Management System is available for new employee
newHire_active = True

# Add a list of employees info
employees = []

# Set counter - Count each employee being added in the system
counter = 0

# Prompt to enter new hire information and verify information


def addEmployeeInfo():
    global counter
    global employees
    global name
    global employeeSSN
    global phone
    global email
    global salary
    global employee_card

    for employee in range(5):
        counter += 1
        name = input("Please provide employee's name: ")
        if name == "":
            print("Please enter information again")
            continue
        employeeSSN = input("Enter SSN #: ")
        if len(employeeSSN) < 9 or len(employeeSSN) > 9:
            print("Please try again")
            continue

        phone = input("Enter phone number: ")
        if len(phone) < 10 or len(phone) > 13:
            print("Please try again")
            continue

        email = input("Enter email address: ")
        r = re.fullmatch(regex, email)
        if not (r):
            print("Please try again")
            continue

        salary = input("Enter salary: $")
        if float(salary) < 0:
            print("Please try again")
            continue
        print(f'''
        --------------{name}---------
        SSN: {employeeSSN}
        Phone: {phone}
        Email: {email}
        Salary: ${salary}
        ---------------------------------''')

        employee_card = name, str(employeeSSN), str(phone), email, str(salary)
        employees.append(list(employee_card))

        if len(employees) == 1:
            print("\n"*2)
            print(f'''There is {counter} employee in the system.''')
            print("\n"*1)
        elif len(employees) > 1:
            print("\n"*2)
            print(f'''There are {counter} employees in the system.''')
            print("\n"*1)


addEmployeeInfo()


# User will be able to print specific employee information from the saved list


def viewEmployeeInfo():
    global searchSSN
    global print_employee
    global updateEmployee
    global response
    while True:
        print_employee = str(input(
            "Search for an employee by their SSN: "))

        searchSSN = {
            1: employees[0][1],
            2: employees[1][1],
            3: employees[2][1],
            4: employees[3][1],
            5: employees[4][1]
        }

        if print_employee == searchSSN[1]:
            print("\n"*20)
            print(f'''You are now viewing {employees[0][0]}'s information
                SSN: {employees[0][1]}
                Phone: {employees[0][2]}
                Email: {employees[0][3]}
                Salary: ${employees[0][4]}
                ''')

            updateEmployee = input("Type Y to update employee information: ")
            if updateEmployee == "Y":
                print("\n"*10)
                print(f'''Which of the following would you like to edit for this employee:
                    Name
                    SSN
                    Phone
                    Email
                    Salary
                ''')
                response = input("Please make a selection: ")

                if response.capitalize() == "Name":
                    print()
                    print("Please enter name change of employee.")

                    updateInfo = input()
                    employees[0][0] = updateInfo
                    # Update SSN
                elif response.upper() == "SSN":
                    print()
                    print("Please enter SSN of employee.")

                    updateInfo = input()
                    employees[0][1] = updateInfo
                    # update phone
                elif response.capitalize() == "Phone":
                    print()
                    print("Please enter phone number of employee.")

                    updateInfo = input()
                    employees[0][2] = updateInfo
                    # update email
                elif response.capitalize() == "Email":
                    print()
                    print("Please enter email address of employee.")

                    updateInfo = input()
                    employees[0][3] = updateInfo
                elif response.capitalize() == "Salary":
                    print()
                    print("Please enter salary of employee.")

                    updateInfo = input()
                    employees[0][4] = updateInfo
                else:
                    break
        if print_employee == searchSSN[2]:
            print("\n"*20)
            print(f'''You are now viewing {employees[1][0]}'s information
                SSN: {employees[1][1]}
                Phone: {employees[1][2]}
                Email: {employees[1][3]}
                Salary: ${employees[1][4]}
            ''')
            updateEmployee = input("Type Y to update employee information: ")
            if updateEmployee.upper() == "Y":
                print("\n"*10)
                print(f'''Which of the following would you like to edit for this employee:
                    Name
                    SSN
                    Phone
                    Email
                    Salary
                ''')
                response = input("Please make a selection: ")
            # If user searched second employee
                if searchSSN[2]:
                    response = input()
                    # Update name
                    if response.capitalize() == "Name":
                        print()
                        print("Please enter name change of employee.")

                        updateInfo = input()
                        employees[1][0] = updateInfo
                        # Update SSN
                    elif response.upper() == "SSN":
                        print()
                        print("Please enter SSN of employee.")

                        updateInfo = input()
                        employees[1][1] = updateInfo
                        # update phone
                    elif response.capitalize() == "Phone":
                        print()
                        print("Please enter phone number of employee.")

                        updateInfo = input()
                        employees[1][2] = updateInfo
                        # update email
                    elif response.capitalize() == "Email":
                        print()
                        print("Please enter email address of employee.")

                        updateInfo = input()
                        employees[1][3] = updateInfo
                    elif response.capitalize() == "Salary":
                        print()
                        print("Please enter salary of employee.")

                        updateInfo = input()
                        employees[1][4] = updateInfo

        if print_employee == searchSSN[3]:
            print("\n"*20)
            print(f'''You are now viewing {employees[2][0]}'s information
                SSN: {employees[2][1]}
                Phone: {employees[2][2]}
                Email: {employees[2][3]}
                Salary: ${employees[2][4]}
            ''')
            updateEmployee = input("Type Y to update employee information: ")
            if updateEmployee.upper() == "Y":
                print("\n"*10)
                print(f'''Which of the following would you like to edit for this employee:
                    Name
                    SSN
                    Phone
                    Email
                    Salary
                ''')
                response = input("Please make a selection: ")
                # If user searched third employee
                if searchSSN[3]:
                    response = input()
                    # Update name
                    if response.capitalize() == "Name":
                        print()
                        print("Please enter name change of employee.")

                        updateInfo = input()
                        employees[2][0] = updateInfo
                        # Update SSN
                    elif response.upper() == "SSN":
                        print()
                        print("Please enter SSN of employee.")

                        updateInfo = input()
                        employees[2][1] = updateInfo
                        # update phone
                    elif response.capitalize() == "Phone":
                        print()
                        print("Please enter phone number of employee.")

                        updateInfo = input()
                        employees[2][2] = updateInfo
                        # update email
                    elif response.capitalize() == "Email":
                        print()
                        print("Please enter email address of employee.")

                        updateInfo = input()
                        employees[2][3] = updateInfo
                        # update salary
                    elif response.capitalize() == "Salary":
                        print()
                        print("Please enter salary of employee.")

                        updateInfo = input()
                        employees[2][4] = updateInfo

        if print_employee == searchSSN[4]:
            print("\n"*20)
            print(f'''You are now viewing {employees[3][0]}'s information
                SSN: {employees[3][1]}
                Phone: {employees[3][2]}
                Email: {employees[3][3]}
                Salary: ${employees[3][4]}
            ''')
            updateEmployee = input("Type Y to update employee information: ")
            if updateEmployee.upper() == "Y":
                print("\n"*10)
                print(f'''Which of the following would you like to edit for this employee:
                    Name
                    SSN
                    Phone
                    Email
                    Salary
                ''')
                response = input("Please make a selection: ")
                # If user searched fourth employee
                if searchSSN[4]:
                    response = input()
                    # Update name
                    if response.capitalize() == "Name":
                        print()
                        print("Please enter name change of employee.")

                        updateInfo = input()
                        employees[3][0] = updateInfo
                        # Update SSN
                    elif response.upper() == "SSN":
                        print()
                        print("Please enter SSN of employee.")

                        updateInfo = input()
                        employees[3][1] = updateInfo
                        # update phone
                    elif response.capitalize() == "Phone":
                        print()
                        print("Please enter phone number of employee.")

                        updateInfo = input()
                        employees[3][2] = updateInfo
                        # update email
                    elif response.capitalize() == "Email":
                        print()
                        print("Please enter email address of employee.")

                        updateInfo = input()
                        employees[3][3] = updateInfo
                        # update salary
                    elif response.capitalize() == "Salary":
                        print()
                        print("Please enter salary of employee.")

                        updateInfo = input()
                        employees[3][4] = updateInfo

        if print_employee == searchSSN[5]:
            print("\n"*20)
            print(f'''You are now viewing {employees[4][0]}'s information
                SSN: {employees[4][1]}
                Phone: {employees[4][2]}
                Email: {employees[4][3]}
                Salary: ${employees[4][4]}
            ''')
            updateEmployee = input("Type Y to update employee information: ")
            if updateEmployee.upper() == "Y":
                print("\n"*10)
                print(f'''Which of the following would you like to edit for this employee:
                    Name
                    SSN
                    Phone
                    Email
                    Salary
                ''')
                response = input("Please make a selection: ")
                #  If user searched fifth employee
                if searchSSN[5]:
                    response = input()
                    # Update name
                    if response.capitalize() == "Name":
                        print()
                        print("Please enter name change of employee.")

                        updateInfo = input()
                        employees[4][0] = updateInfo
                        # Update SSN
                    elif response.upper() == "SSN":
                        print()
                        print("Please enter SSN of employee.")

                        updateInfo = input()
                        employees[4][1] = updateInfo
                        # update phone
                    elif response.capitalize() == "Phone":
                        print()
                        print("Please enter phone number of employee.")

                        updateInfo = input()
                        employees[4][2] = updateInfo
                        # update email
                    elif response.capitalize() == "Email":
                        print()
                        print("Please enter email address of employee.")

                        updateInfo = input()
                        employees[4][3] = updateInfo
                        # update salary
                    elif response.capitalize() == "Salary":
                        print()
                        print("Please enter salary of employee.")

                        updateInfo = input()
                        employees[4][4] = updateInfo
        break


viewEmployeeInfo()


def viewAllEmployees():
    global answer
    print("\n" * 2)
    print("Would you like to view all employees?")
    answer = input("Y/N: ")

    if answer.upper() == "Y":
        for i in range(len(employees)):
            print()
            print(", ".join(employees[i]))
            print()
    elif answer.upper() == "N":
        print("Thank you!")
        print()
        print()


viewAllEmployees()


def employeeData():
    saveInformation = input("Type Y to save each employees information: ")
    if saveInformation.upper() == "Y":

        with open("employees.txt", "a") as f:
            for employee in employees:
                f.write("%s\n" % employee)
        with open("employees.txt", "r") as fs:
            file1 = fs.read()

    # Import data into file
    importPrompt = input("Type Y to import a file: ")
    if importPrompt.upper() == "Y":
        fileName = input("Please enter the filename, with .txt: ")
        with open(fileName, "a") as file2:
            file2.write("\n")
            file2.write(file1)


employeeData()
