# =====importing libraries===========
file = open("user.txt", "r+")
file2 = open("tasks.txt", "r+")
from datetime import date         # this function gets the current date and time
today = date.today()
daysDate = today.strftime("%d %B %Y")


# ====Login Section====
""" user name section asks user for username and password and stores in in a user variable """
userName = input("enter your user name: ")
password = input("enter your password: ")
user = userName + ", " + password

'''checkUser checks if the user name is in the file'''
checkUser = file.readlines()

'''if its not in the file prompt the user to try again'''
while user not in checkUser:
    print("username and password incorrect")
    userName = input("enter username: ")
    password = input("enter password: ")
    user = userName + ", " + password
file.close()

'''if user name in file give the menu'''
# Admin menu
while True:
  if userName == "admin":

    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
s - statistics
: ''').lower()
# Regular user menu
  else:
    menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

# register user
  if menu == 'r':
    if userName == "admin":
        '''open user file, welcome the user and allow for a new username and password'''
        file = open("user.txt", "a")
        print("Welcome new user!")
        '''username and password inputs'''
        newUsername = input("create username: ")
        newPassword = input("create password: ")
        conPassword = input("confirm password: ")

        '''if passwords do not match loop and prompt user to enter the correct password'''
        if newPassword != conPassword:
            while newPassword != conPassword:
                conPassword = input("passwords do not match enter again: ")

            '''once correct store username and password in newUser variable'''
            newUser = newUsername + ", " + newPassword

            '''welcome new user'''
            print("welcome {} \n".format(newUsername))

            '''add new user to user file'''
            file.write(str(newUser + "\n"))

        # if inputs are correct:
        else:
            """add user name and password together and store it in newUser"""
            newUser = newUsername+", "+newPassword

            '''welcome the user'''
            print("welcome {}".format(newUsername))

            '''add user to user file'''
            file.write(str("\n"+newUser))
            file.close()

    else:   # if user not admin display this message
            print("Sorry only admins can register new users :( ")
            pass


  elif menu == 'a':
    file2 = open("tasks.txt", "a")
    taskUser = input("who would you like to assign a task to: ")
    taskName = input("enter the title of the task: ")
    taskDes = input("enter a description of the task: ")
    dueDate = input("enter the due date of the task: ")
    TheDate = today
    complete = "no"
    file2.write("\n" + taskUser + ", " + taskName + ", " + taskDes + ", " + dueDate + ", " + daysDate + ", " + complete)
    file2.close()
    pass


  elif menu == 'va':
        file2 = open("tasks.txt", "r")
        for i in file2:
            viewAll = i.split(",")

            print(f'''
Task:               {viewAll[1]}
assigned to:         {viewAll[0]} 
date assigned:      {viewAll[3]}
due date:           {viewAll[4]}
task complete:      {viewAll[5]}
task description    {viewAll[2]}
''''')
        file2.close()
        pass


  elif menu == 'vm':
        file2 = open("tasks.txt", "r")
        for i in file2:
            viewAll = i.split(",")
            if userName == viewAll[0]:
                print(f'''
Task:               {viewAll[1]}
assigned to:         {viewAll[0]} 
date assigned:      {viewAll[3]}
due date:           {viewAll[4]}
task complete:      {viewAll[5]}
task description    {viewAll[2]}
                ''''')
        else:
            print("no tasks assigned")

        pass


  elif menu == 'e':
        print('Goodbye!!!')
        file2 = open("tasks.txt", "a")
        import sys
        output = ""
        with open("tasks.txt", "r+") as fy:
            for l in fy:
                if not l.isspace():
                    output += l
        fy = open("tasks.txt", "w")
        fy.write(output)
        exit()

  elif menu == "s":
    file2 = open("tasks.txt", "r")
    file = open("user.txt", "r")

    with open("tasks.txt", "r") as fp:
        x = len(fp.readlines())
        print('Total tasks:', x)

    with open("user.txt", "r") as fa:
        lUsers = len(fa.readlines())
        print(f'''total users: {lUsers}
''')


  else:
        print("You have made a wrong choice, Please Try again")
