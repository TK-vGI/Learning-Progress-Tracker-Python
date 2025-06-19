# Stage 4
import re  # imports regular expressions module

# Global variables
students = []

# List of correct commands
commands = ['exit', 'add students', 'back', 'list', 'add points', 'find', 'statistics']
# Stage 1
cmd_exit = "exit"
# Stage 2
cmd_add_students = "add students"
cmd_back = "back"
# Stage 3
cmd_list = "list"
cmd_add_points = "add points"
cmd_find = "find"
# Stage 4
cmd_stats = "statistics"

# List of courses
# ['Python', 'Data Structures and Algorithms', 'Databases', 'Flask']
courses = ['Python', 'DSA', 'Databases', 'Flask']
max_points = {'Python': 600, 'DSA': 400, 'Databases': 480, 'Flask': 550}

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
msg_10 = "Type the name of a course to see details or 'back' to quit"
msg_101 = "Unknown course"


class Student:
    """Class handles information (credentials, actual course/scores) about a student."""

    def __init__(self, student_id, first_name, last_name, email):
        # self.id = str(hash(email))
        self.id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.score_python = 0
        self.score_dsa = 0
        self.score_db = 0
        self.score_flask = 0
        # Track submissions for activity calculation
        self.submissions = {'Python': 0, 'DSA': 0, 'Databases': 0, 'Flask': 0}

    def full_name(self):
        """Return full name of student."""
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        """Prints full credentials of student."""
        return f"{self.id} {self.first_name} {self.last_name} {self.email}"

    # def __hash__(self):
    #     return hash(self.id)

    def __eq__(self, other):
        """Comparison of instances equality based on attribute values."""
        if isinstance(other, Student):
            return self.id == other.id
        return False

    # dictionary-based lookup that retrieves a value based on the key provided in course
    # If course is not in the dictionary, it will raise a KeyError. Can use .get(course, default_value)
    # syntax: {'key1':value1, ... }.get(course, "Course not found")
    def get_points(self, course):
        """Return points for a given course."""
        return {
            'Python': self.score_python,
            'DSA': self.score_dsa,
            'Databases': self.score_db,
            'Flask': self.score_flask
        }[course]

    def is_enrolled(self, course):
        """Check if student is enrolled in a course (non-zero points)."""
        return self.get_points(course) > 0

    def add_submission(self, course, points):
        """Increment submission count for a course if points are added."""
        if points > 0:
            self.submissions[course] += 1


def stats(prt_msg=True):
    if prt_msg:
        print(msg_10)  # "Type the name of a course to see details or 'back' to quit"
        stats_overview()
    while True:
        try:
            inp_stats = input().strip()  # no lower() - names can start with capital letters.
        except KeyboardInterrupt:
            print("\nInput interrupted. Returning to main menu...")
            take_input()
            return
        if inp_stats == cmd_back:
            take_input()
            return
        # Normalize course input
        course_map = {
            'python': 'Python',
            'dsa': 'DSA',
            'databases': 'Databases',
            'flask': 'Flask'
        }
        course = course_map.get(inp_stats.lower(), inp_stats)
        if course not in courses:
            print(msg_101)  # "Unknown course"
        else:
            print_course_stats(course)


def print_course_stats(course):
    """Print statistics for a specific course, including top learners."""
    enrolled_students = [s for s in students if s.is_enrolled(course)]
    # Print header
    print(f"{course}\nid    points    completed")
    # Print top learners with points and completion percentage
    if enrolled_students:
        sorted_students = sorted(
            enrolled_students,
            key=lambda s: (-s.get_points(course), s.id)
        )
        for student in sorted_students:
            points = student.get_points(course)
            completion = round((points / max_points[course]) * 100, 1)
            print(f"{student.id:<6} {points:<10} {completion}%")


def stats_overview():
    """Calculate and display course statistics."""
    if not students:
        print("""Most popular: n/a
Least popular: n/a
Highest activity: n/a
Lowest activity: n/a
Easiest course: n/a
Hardest course: n/a""")
        return

    # Calculate enrollments
    enrollments = {course: sum(1 for s in students if s.is_enrolled(course)) for course in courses}

    # Calculate activity (total submissions)
    activity = {course: sum(s.submissions[course] for s in students) for course in courses}

    # Calculate average grade per submission
    avg_grades = {}
    for course in courses:
        total_points = sum(s.get_points(course) for s in students)
        total_submissions = sum(s.submissions[course] for s in students)
        avg_grades[course] = total_points / total_submissions if total_submissions > 0 else 0

    # Find most and least popular courses
    max_enrollment = max(enrollments.values()) if enrollments else 0
    min_enrollment = min(enrollments.values()) if enrollments else 0
    most_popular = [c for c, e in enrollments.items() if e == max_enrollment and e > 0]
    least_popular = [c for c, e in enrollments.items() if e == min_enrollment and c not in most_popular]

    # Find highest and lowest activity
    max_activity = max(activity.values()) if activity else 0
    min_activity = min(activity.values()) if activity else 0
    highest_activity = [c for c, a in activity.items() if a == max_activity and a > 0]
    lowest_activity = [c for c, a in activity.items() if a == min_activity and c not in highest_activity]

    # Find easiest and hardest courses
    valid_grades = {c: g for c, g in avg_grades.items() if g > 0}
    max_grade = max(valid_grades.values()) if valid_grades else 0
    min_grade = min(valid_grades.values()) if valid_grades else 0
    easiest = [c for c, g in valid_grades.items() if g == max_grade]
    hardest = [c for c, g in valid_grades.items() if g == min_grade and c not in easiest]

    # Format output
    def format_list(lst):
        return ', '.join(lst) if lst else 'n/a'

    print(f"""Most popular: {format_list(most_popular)}
Least popular: {format_list(least_popular)}
Highest activity: {format_list(highest_activity)}
Lowest activity: {format_list(lowest_activity)}
Easiest course: {format_list(easiest)}
Hardest course: {format_list(hardest)}""")


# Verifies the input, if correct name and email address or prints error messages.
# Adds valid credential to a list as [first_name, last_name, email].
# Can call go_back() function.
def add_students(prt_msg=True):
    if prt_msg:
        print(msg_2)  # "Enter student credentials or 'back' to return:"
    while True:
        try:
            inp_add_students = input().strip()  # no lower() - names can start with capital letters.
        except KeyboardInterrupt:
            print("\nInput interrupted. Returning to main menu...")
            take_input()
            return

        credentials = inp_add_students.split(" ")
        if credentials == [cmd_back]:
            go_back()
            break
        elif len(credentials) < 3:
            print(msg_4)  # "Incorrect credentials"
            continue
        else:
            # Splits complicated credentials. Creates a list: [first_name, last_name, email].
            f_name = credentials[0]
            l_name = " ".join(credentials[1:-1])  # all between the first and last "space" char assigned as last name
            email = credentials[-1]
            user = [f_name, l_name, email]
            # print(user)
            if not verify_name(user[0]):
                print(msg_41)  # "Incorrect first name."
                continue
            elif not verify_name(user[1]):
                print(msg_42)  # "Incorrect last name."
                continue
            elif not verify_email(user[2]):
                print(msg_43)  # "Incorrect email."
                continue
            elif any(s.email == email for s in students):
                print(msg_6)  # "This email is already taken."
                continue
            # creates 5-digit integer identification
            student_id = str(new_id())
            # creates an instance of Student class and appends to the list of students
            students.append(Student(student_id, f_name, l_name, email))
            print(msg_3)  # "The student has been added."


def go_back():
    print(msg_5.format(len(students)))  # "Total {n} students have been added."
    print(msg_1)  # "Enter 'exit' to exit the program"
    take_input()


# Matches() str(name) with the regexp pattern. Returns True if it matches, False otherwise.
def verify_name(name):
    name_pattern = r"^[A-Za-z](?:[A-Za-z]+|['-][A-Za-z]+)(?: [A-Za-z](?:[A-Za-z]+|['-][A-Za-z]+))*$|^[A-Za-z]{2,}(?:['-][A-Za-z]+)*(?: [A-Za-z]{2,}(?:['-][A-Za-z]+)*)*$"
    return bool(re.fullmatch(name_pattern, name))


# Matches() str(email) with the regexp pattern. Returns True if it matches, False otherwise.
def verify_email(email):
    # email_pattern = '^[a-zA-Z0-9]+(?:[.][a-zA-Z0-9]+)?@[a-zA-Z0-9]+[.][a-zA-Z0-9]+$'
    email_pattern = '^[a-zA-Z0-9]+(?:[.][a-zA-Z0-9]+)*@[a-zA-Z0-9]+(?:[.][a-zA-Z0-9]+)+$'
    return bool(re.fullmatch(email_pattern, email))


# Returns a unique 5-digit number as id for a new added student.
def new_id():
    if len(students) != 0:
        new_number = int(students[-1].id) + 1
    else:
        new_number = 10000
    return new_number


# Prints/lists all students by id numbers or prints an error message.
def list_students():
    if len(students) == 0:
        print(msg_71)  # "No students found."
    else:
        print(msg_7)  # "Students:"
        for student in students:
            print(student.id)
    take_input()


# Finds a student by its id number and lists its course scores
def find_students(prt_msg=True):
    if prt_msg:
        print(msg_9)  # "Enter an id or 'back' to return"
    while True:
        try:
            inp_find_students = input().strip().lower()
        except KeyboardInterrupt:
            print("\nInput interrupted. Returning to main menu...")
            take_input()
            return

        if inp_find_students == cmd_back:
            go_back()
            return
        else:
            student = next((s for s in students if s.id == inp_find_students), None)
            # print(student.full_name())
            if student is None:
                print(msg_81 % inp_find_students)  # "No student is found for id=%s"
            else:
                print(msg_91 % (inp_find_students, student.score_python, student.score_dsa, student.score_db,
                                student.score_flask))
                # "%s points: Python=%d; DSA=%d; Databases=%d; Flask=%d"


# Matches() str(input) with the regexp pattern. Returns True if it matches, False otherwise.
def verify_int_number(numbers):
    # input pattern = 'studentId number number number number'
    numbers_pattern = "[a-zA-Z0-9]+ [0-9]+ [0-9]+ [0-9]+ [0-9]+"
    return bool(re.fullmatch(numbers_pattern, numbers))


# Checks if the list of students contains student_id. Returns True if it matches, False otherwise.
def verify_student(std_id):
    stdnt = next((s for s in students if s.id == std_id), None)
    return stdnt


# Verifies the input, if correct ID and score-points or prints error messages.
# Adds valid score-points to valid student ID.
# Can call go_back() function.
def add_points(prt_msg=True):
    if prt_msg:
        print(msg_8)  # "Enter an id and points or 'back' to return."
    while True:
        try:
            inp_points = input().strip().lower()
        except KeyboardInterrupt:
            print("\nInput interrupted. Returning to main menu...")
            take_input()
            return
        if inp_points == cmd_back:
            go_back()
            return
        if not verify_int_number(inp_points):
            print(msg_82)  # "Incorrect points format."
            continue

        add_points_ = inp_points.split(" ")
        std_id = add_points_[0]
        points = [int(x) for x in add_points_[1:]]
        student = verify_student(std_id)
        if student is None:
            print(msg_81 % std_id)
            continue
        student = verify_student(std_id)
        if student is None:
            print(msg_81 % std_id)  # "No student is found for id=%s"
            continue
        student.score_python += int(points[0])
        student.score_dsa += int(points[1])
        student.score_db += int(points[2])
        student.score_flask += int(points[3])
        # Update submission counts
        student.add_submission('Python', points[0])
        student.add_submission('DSA', points[1])
        student.add_submission('Databases', points[2])
        student.add_submission('Flask', points[3])
        print(msg_83)  # "Points updated."


# Main interface of the program. Cycle through valid commands else prints the error message.
def take_input():
    # Note: Course names like 'Python', 'DSA', etc., are not in the 'commands' list,
    # so entering them directly will trigger "Error: unknown command!" as required.
    # print("Available commands: add students, list, add points, find, statistics, back, exit")
    # User command input - stripped and lowercased
    while True:
        try:
            usr_inp = input().strip().lower()
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting...")
            exit(0)
        if usr_inp == "":
            print('No input.')
            continue
        if usr_inp not in commands:
            print("Error: unknown command!")
            continue
        elif usr_inp == cmd_exit:
            print('Bye!')
            exit()
        elif usr_inp == cmd_back:
            print(msg_1)
            continue
        elif usr_inp == cmd_add_students:
            add_students()
        elif usr_inp == cmd_list:
            list_students()
        elif usr_inp == cmd_add_points:
            add_points()
        elif usr_inp == cmd_find:
            find_students()
        elif usr_inp == cmd_stats:
            stats()


# Run the program
print("Learning progress tracker")
take_input()

# End of Stage 4
