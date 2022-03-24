from lib.PyAutoClassroom import Student

Student = Student('vlad.gavanescu@cnodobescu.ro', 'Vlad2020', True)
Student.login()
Student.enter_course('Limba Romana' )
Student.__exit__()