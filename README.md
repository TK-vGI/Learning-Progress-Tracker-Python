# Learning-Progress-Tracker-Python
We are going to create a program that keeps track of the learning progress of multiple students.
To accomplish this task, we should teach our program to read various data in string and numeric formats,
do certain calculations, and output desired information. To begin with, we need to make our program interactive.

1. Stage 1 - No empty lines here
    - Demonstrate that it is running by printing its title: Learning Progress Tracker.
    - Wait for the commands. In this stage, the only command the program should recognize is exit.
      Once a user enters it, the program should print Bye! and quit.
    - Detect if a user has entered a blank line and print No input in response.
    - Print Unknown command! if a user enters an unknown command.

2. Stage 2 - Verify new users
    - Recognize a new command: add students and respond with the following message: Enter student credentials or
      'back' to return.
    - Recognize a new back command and react as follows: if users want to finish adding new students,
      the program should print a message with the total number of students added during the session,
      for example: Total 5 students have been added. Otherwise, print a hint: Enter 'exit' to exit the program.
    - The program should read user credentials from the console and check whether they match the established patterns.
      If the credentials match all patterns, print The student has been added. Otherwise, it should print which
      part of the credentials is not acceptable: Incorrect first name, Incorrect last name and Incorrect email.
    - If the input cannot be interpreted as valid credentials, the program should print Incorrect credentials.

3. Stage 3 - A detailed record
    - Check if the provided email has been already used when adding information about students. If so,
      respond with the following message: This email is already taken.
    - Recognize the new list command to print the Students: a header followed by the student IDs. The students
      must be listed in the order they were added. Remember, each ID must be unique. If there are no students
      to list, print No students found.
    - Recognize the new add points and print the following message in response: Enter an id and points or
      'back' to return. After that, the program must read learning progress data in the following format:
      studentId number number number number. The numbers correspond to the courses (Python, DSA, Databases, Flask).
      Number is a non-negative integer number. If there is no student with the specified ID, the program should
      print No student is found for id=%s. where %s is the invalid ID. Also, if any of the numbers are missing,
      or there is an extra number or any of the numbers do not meet the requirements mentioned above, the program
      should print Incorrect points format. If the learning progress data is entered in the correct format,
      and the specified user exists, the program should update the student's record and print Points updated.
      Once back is entered, the program must stop reading learning progress data.
    - Recognize the find command and print the following message: Enter an id or 'back' to return. After that,
      if an ID is entered, the program should either print details of the student with the specified ID
      in this format: id points: Python=%d; DSA=%d; Databases=%d; Flask=%dwhere %d is the respective number of
      points earned by the student. If the ID cannot be found, print the error message: No student is found
      for id=%s. where %s is the invalid ID.

4. Stage 4 - Retrieving statistics 
   - Add a new command to your program's toolkit: statistics. If users enter this command, your program should
     output the header: Type the name of a course to see details or 'back' to quit and six lines with the following
     information: Most popular, Least popular, Highest activity, Lowest activity, Easiest course, Hardest course
     with the names of the corresponding courses. After that, if users enter a course name, the program should
     display the details of this course, but if users enter a name that doesn't correspond to any of the courses,
     the program should print Unknown course. When the back command is entered, the program goes back to other
     available commands.
   - When users enter the statistics command, your program must display the details about any course. When users
     type in the name of a course, the program should display the name of the course in the first line, then the
     column headers, and a list of student IDs, their total points in the respective course, and the percent of
     completion (one decimal place precision). If a course has no students, output only the name of the course and
     the column headers.
   - Course details are available only after users enter statistics, they should not be available with the back.
     If users type in any course name before entering the statistics command, the program must respond with the
     Unknown command! message.
   - Sort student lists by the total number of points in descending order and then by the ID in ascending order.

5. Stage 5 - Notification service
   - Add a new command to your program: notify. When users enter this command, your program should print a
     list of messages to students in the format above. Below the list, print the total number of students that
     should be notified, for example: Total 5 students have been notified.
   - Make sure that your program generates only one notification for each trigger event. The trigger event is
     the completion of any course by a student.
   - The messages generated by your program must contain the personal information of the students, such as
     an email address and the full name, as well as the name of the relevant course, if applicable.