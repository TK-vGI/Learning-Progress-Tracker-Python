# # Stage 1
# print("Learning progress tracker")
#
# # User command input - stripped and lowercased
# inp = input().strip().lower()
#
# # Loops until user enters 'exit'
# while inp != 'exit':
#     if not inp and not inp.isalpha():
#         print('No input.')
#     else:
#         print('Error: unknown command!')
#     inp = input().strip().lower()
#
# print('Bye!')
#
# # End of Stage 1


# # Stage 2
# import re # imports regular expressions module
#
# # Course title
# print("Learning progress tracker")
#
# # Global variables
# # total_students = 0 # not used
#
# # List of correct commands
#  = ['exit', 'add students', 'back']
#
# # List of input and/or error messages
# msg_1 = "Enter 'exit' to exit the program."
# msg_2 = "Enter student credentials or 'back' to return:"
# msg_3 = "The student has been added."
# msg_4 = "Incorrect credentials."
# msg_41 = "Incorrect first name."
# msg_42 = "Incorrect last name."
# msg_43 = "Incorrect email."
# msg_5 = "Total {} students have been added."
#
#
# # Calls process_credentials() and verifies the input. Prints error messages.
# # Returns a valid credential as a list: [first_name, last_name, email] or -1.
# def add_students(user_input):
#     # print('inside add_students function')
#     credentials = list(user_input.split(" "))
#     if len(credentials) < 3:
#         print(msg_4)
#         return -1
#     else:
#         user = process_credentials(credentials)
#     # print(user)
#     if not verify_name(user[0]):
#         print(msg_41)
#         return -1
#     elif not verify_name(user[1]):
#         print(msg_42)
#         return -1
#     elif not verify_email(user[2]):
#         print(msg_43)
#         return -1
#     else:
#         print(msg_3)
#         return user
#
#
# # Splits complicated credentials. Returns a list: [first_name, last_name, email].
# Def process_credentials(cred):
#     # print('inside process_credentials function')
#     f_name = cred[0]
#     l_name = " ".join(cred[1:-1])
#     email = cred[-1]
#     return [f_name, l_name, email]
#
#
# # Matches() str(name) with the regexp pattern. Returns True if it matches, False otherwise.
# def verify_name(name):
#     # print('inside verify_name function')
#     name_pattern = "[A-Za-z]['-]?[A-Za-z]+(?:[ '-][A-Za-z]+)*"
#     return bool(re.fullmatch(name_pattern, name)
#                 )
#
#
# # Matches() str(email) with the regexp pattern. Returns True if it matches, False otherwise.
# def verify_email(email):
#     # print('inside verify_email function')
#     email_pattern = '^[a-zA-Z0-9]+(?:[.][a-zA-Z0-9]+)?@[a-zA-Z0-9]+[.][a-zA-Z0-9]+$'
#     return bool(re.fullmatch(email_pattern, email))
#
#
# # User command input - stripped and lowercased
# inp = input().strip().lower()
#
# # Loops until user enters 'exit'
# while inp != 'exit':
#     if not inp and not inp.isalpha():
#         print('No input.')
#     elif inp not in commands:
#         print('Error: unknown command!')
#     elif inp == 'back':
#         print(msg_1)
#     elif inp == 'add students':
#         new_students = 0
#         print(msg_2)
#         inp = input().strip()  # no lower() - names can start with capital letters.
#
#         # Loops until the user enters 'back'. Adds/processes students during the session.
#         while inp.lower() != 'back':
#             if add_students(inp) != -1:
#                 new_students += 1
#             inp = input().strip()
#
#         # prints number of students added during the session
#         print(msg_5.format(new_students))
#         # # adds the session to global total_students
#         # total_students += new_students # not used
#
#     # User input for the main outer loop.
#     inp = input().strip().lower()
#
# print('Bye!')
#
# # End of Stage 2


# Stage 3
import re  # imports regular expressions module

# Global variables
students = []

# List of correct commands
commands = ['exit', 'add students', 'back', 'list', 'add points', 'find']
cmd_exit = "exit"
cmd_add_students = "add students"
cmd_back = "back"
cmd_list = "list"
cmd_add_points = "add points"
cmd_find = "find"

# List of courses
courses = ['Python', 'Data Structures and Algorithms', 'Databases', 'Flask']

# List of input and/or error messages
msg_1 = "Enter 'exit' to exit the program."
msg_2 = "Enter student credentials or 'back' to return:"
msg_3 = "The student has been added."
msg_4 = "Incorrect credentials."
msg_41 = "Incorrect first name."
msg_42 = "Incorrect last name."
msg_43 = "Incorrect email."
msg_5 = "Total {} students have been added."
msg_6 = "This email is already taken."
msg_7 = "Students:"
msg_71 = "No students found."
msg_8 = "Enter an id and points or 'back' to return."
msg_81 = "No student is found for id=%s."
msg_82 = "Incorrect points format."
msg_83 = "Points updated."
msg_9 = "Enter an id or 'back' to return"
msg_91 = "%s points: Python=%d; DSA=%d; Databases=%d; Flask=%d"

class Student:
    def __init__(self,student_id, first_name, last_name, email):
        # self.id = str(hash(email))
        self.id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.score_python = 0
        self.score_dsa = 0
        self.score_db = 0
        self.score_flask = 0


    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name} {self.email}"


    # def __hash__(self):
    #     return hash(self.id)


    def __eq__(self, other):
        if isinstance(other, Student):
            return self.id == other.id
        return False


# Verifies the input, if correct name and email address or prints error messages.
# Adds valid credential to a list as [first_name, last_name, email].
# Can call go_back() function.
def add_students(prt_msg=True):
    # print('inside add_students function')
    if prt_msg:
        print(msg_2) # "Enter student credentials or 'back' to return":

    inp_add_students = input().strip()  # no lower() - names can start with capital letters.
    credentials = inp_add_students.split(" ")

    if credentials == [cmd_back]:
        go_back()
    elif len(credentials) < 3:
        print(msg_4) # "Incorrect credentials"
        add_students(False)
    else:
        # Splits complicated credentials. Creates a list: [first_name, last_name, email].
        credentials_ = list(credentials)  # temp variable
        f_name = credentials_[0]
        l_name = " ".join(credentials_[1:-1])  # all between the first and last "space" char assigned as last name
        email = credentials_[-1]
        user = [f_name, l_name, email]
        credentials_.clear()  # clear values in temp variable
        # print(user)
        if not verify_name(user[0]):
            print(msg_41)  # "Incorrect first name."
            add_students(False)
        elif not verify_name(user[1]):
            print(msg_42)  # "Incorrect last name."
            add_students(False)
        elif not verify_email(user[2]):
            print(msg_43)  # "Incorrect email."
            add_students(False)
        elif any(s.email == email for s in students):
            print(msg_6)  # "This email is already taken."
            add_students(False)
        else:
            # creates 5-digit integer identification
            student_id = str(new_id())
            # creates an instance of Student class and appends to the list of students
            students.append(Student(student_id, f_name, l_name, email))
            print(msg_3)  # "The student has been added."
            add_students(False)


def go_back():
    print(msg_5.format(len(students))) # "Total {n} students have been added."
    print(msg_1) # "Enter 'exit' to exit the program"
    take_input()


# Matches() str(name) with the regexp pattern. Returns True if it matches, False otherwise.
def verify_name(name):
    # print('inside verify_name function')
    name_pattern = "[A-Za-z]['-]?[A-Za-z]+(?:[ '-][A-Za-z]+)*"
    return bool(re.fullmatch(name_pattern, name))


# Matches() str(email) with the regexp pattern. Returns True if it matches, False otherwise.
def verify_email(email):
    # print('inside verify_email function')
    email_pattern = '^[a-zA-Z0-9]+(?:[.][a-zA-Z0-9]+)?@[a-zA-Z0-9]+[.][a-zA-Z0-9]+$'
    return bool(re.fullmatch(email_pattern, email))


# Returns a unique 5-digit number as id for a new added student.
def new_id():
    # print('inside new_id function')
    if len(students) != 0:
        new_number = int(students[-1].id) + 1
    else:
        new_number = 10000
    return new_number


# Prints/lists all students by id numbers or prints an error message.
def list_students():
    # print('inside list_students function')
    if len(students) == 0:
        print(msg_71) # "No students found."
    else:
        print(msg_7) # "Students:"
        for student in students:
            print(student.id)
    take_input()


# Finds a student by its id number and lists its course scores
def find_students(prt_msg=True):
    # print('inside find_students function')
    if prt_msg:
        print(msg_9) # "Enter an id or 'back' to return"

    inp_find_students = input().strip().lower()
    if inp_find_students == cmd_back:
        take_input()
    else:
        student = next((s for s in students if s.id == inp_find_students), None)
        # print(student.full_name())
        if student is None:
            print(msg_81 % inp_find_students) # "No student is found for id=%s"
        else:
            print(msg_91 % (inp_find_students, student.score_python, student.score_dsa, student.score_db, student.score_flask))
            # "%s points: Python=%d; DSA=%d; Databases=%d; Flask=%d"
    find_students(False)


# Matches() str(input) with the regexp pattern. Returns True if it matches, False otherwise.
def verify_int_number(numbers):
    # input pattern = 'studentId number number number number'
    numbers_pattern = "[-A-Za-z0-9]+ [0-9]+ [0-9]+ [0-9]+ [0-9]+"
    return bool(re.fullmatch(numbers_pattern, numbers))


# Checks if the list of students contains student_id. Returns True if it matches, False otherwise.
def verify_student(std_id):
    stdnt = next((s for s in students if s.id == std_id), None)
    return stdnt


# Verifies the input, if correct ID and score-points or prints error messages.
# Adds valid score-points to valid student ID.
# Can call go_back() function.
def add_points(prt_msg=True):
    # print('inside add_points function')
    if prt_msg:
        print(msg_8)  # "Enter an id and points or 'back' to return."

    inp_points = input().strip().lower()
    if inp_points == cmd_back:
        take_input()
    elif not verify_int_number(inp_points):
        print(msg_82)  # "Incorrect points format."
        add_points(False)
    else:
        add_points_ = inp_points.split(" ")
        std_id = add_points_[0]
        student = verify_student(std_id)
        if student is None:
            print(msg_81 % std_id)  # "No student is found for id=%s"
            add_points(False)
        else:
            student.score_python += int(add_points_[1])
            student.score_dsa += int(add_points_[2])
            student.score_db += int(add_points_[3])
            student.score_flask += int(add_points_[4])
            print(msg_83)  # "Points updated."
            add_points(False)


# Main interface of the program. Cycle through valid commands else prints the error message.
def take_input():
    # print('inside take_input function')
    # User command input - stripped and lowercased
    usr_inp = input().strip().lower()

    if not usr_inp and not usr_inp.isalpha():
        print('No input.')
        take_input()
    elif usr_inp == cmd_exit:
        print('Bye!')
        exit()
    elif usr_inp == cmd_back:
        print(msg_1)
        take_input()
    elif usr_inp == cmd_add_students:
        add_students()
    elif usr_inp == cmd_list:
        list_students()
    elif usr_inp == cmd_add_points:
        add_points()
    elif usr_inp == cmd_find:
        find_students()
    else:
        print("Error: unknown command!")
        take_input()


# Run the program
print("Learning progress tracker")
take_input()

# End of Stage 3