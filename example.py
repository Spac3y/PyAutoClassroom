from lib.PyAutoClassroom import Student

Student = Student('usr, 'pass', True)
Student.login()
Student.enter_course('Class' )
Student.__exit__()
