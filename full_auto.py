from lib.PyAutoClassroom import Student

flist = []

string = input('Enter your class name you want to enter: ')
flist.append(string)

confirm = input('Do you want to add more classes? Y/N ')
while confirm.upper() == 'Y':
    strng = input('Enter your class name you want to add to qeueu: ')
    confirm = input('Do you want to add more classes? Y/N ')
    flist.append(strng)

print('Entering these classes: ')
for i in range(len(flist)):
    print(flist[i])

Student= Student('email', 'pass')
Student.login()

for i in flist:
    Student.enter_course(i)
    Student.exit_class()

Student.exiting()
