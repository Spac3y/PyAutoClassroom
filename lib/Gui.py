import json
import os
from tkinter import *
import PIL.Image
import PIL.ImageTk
from PyAutoClassroom import Student

if os.name !='nt':
    exit()

#Json Loader
dirname = str(os.path.dirname(__file__))

data_json = open(dirname + '\\data\\info.json')
classes_json = open(dirname + '\\data\\classes.json')
data = json.load(data_json)
classes_load = json.load(classes_json)
data_json.close()
classes_json.close()

#Main GUI
root = Tk()

state = NORMAL

main_window_settings = {
    root.iconbitmap(dirname + '\\Photos\\icon.ico'),
    root.title('PyAutoClassroom'),
    root.geometry('500x500'),
    root.minsize(500,500),
    root.maxsize(500,500),
    # root.configure(background = '#24292e'),
    }

photos = {
    # 'travis_scott' : PIL.ImageTk.PhotoImage(PIL.Image.open(dirname + '\\Photos\\travisscott.jpg').resize((200,200))),    
    'execute_code_image' : PIL.ImageTk.PhotoImage(PIL.Image.open(dirname + "\\Photos\\download.png").resize((40,40))),
    'rick_roll' : PIL.ImageTk.PhotoImage(PIL.Image.open(dirname + '\\Photos\\rickroll.png'))}

text_input = Entry(root, bd=2, width=50,state=state)
text_input.place(
    relx=0.315,
    rely=0.0,
    anchor='n')
text_input.insert(0, 'Classes:')

#Emai entry
email_entry = Entry(root, width=24, bd=2,state=state)
email_entry.place(
    relx=0.159,
    rely=0.05,
    anchor="n")
email_entry.insert(0, str(data["email"]))

#Password entry
password_entry = Entry(root, width=24, bd=2,state=state)
password_entry.place(
    relx=0.472,
    rely=0.05,
    anchor="n")
password_entry.insert(0, ''.join('*' for i in range(len(data["password"]))))

def execute_code():
    student_load = Student(str(data["email"]),str(data["password"]))
    student_load.login()
    
def first_time_setup():
    pass

def add_to_queue():
    global flist
    flist = []
    var = ''
    txtinput = str(text_input.get())
    for i in txtinput:
        if i.isspace():
            flist.append(var)
            var = ''
        else:
            var = var + i
    flist.append(var)
    print(flist)

def save_login_def():
    data_json = open(dirname + '\\data\\info.json','w')
    data["email"] = str(email_entry.get())
    data["password"] = str(password_entry.get())
    json.dump(data,data_json)
    data_json.close()
    password_entry.delete(0,END)
    password_entry.insert(0, ''.join('*' for i in range(len(data["password"]))))

execute_button = Button(root,command = execute_code,padx=50, pady=50, image=photos['execute_code_image'])
execute_button.place(
    relx = 0.58,
    rely=0.594,
    anchor='center')


exit_button_enter = Button(root, command=root.destroy, text = 'Exit',padx=10,pady=5)
exit_button_enter.place(
    relx=0.055,
    rely=0.605,
    anchor='center')


console_output = Label(root, text = 'test console output!!!', padx=188, pady=78,background='#24292e', fg='white', bd=3, relief='flat')
console_output.place(
    relx=0.005,
    rely=0.998,
    anchor='sw')


class_queue = Label(root, bg='#24292e', bd=2, padx=88, pady=150, relief='flat')
class_queue.place(
    relx=0.989,
    rely=0.32,
    anchor='e')

save_login_info = Button(root, text='Login', padx=13,pady=5, command=save_login_def,state=state)
save_login_info.place(
    relx=0.557,
    rely=0.2,
    anchor='center')

add_to_queue_button = Button(root, text='Save', padx=15, pady=5, relief='raised', command=add_to_queue,state=state)
add_to_queue_button.place(
    relx=0.557,
    rely=0.094,
    anchor='n')

root.mainloop()
