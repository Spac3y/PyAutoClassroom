from file_mover import *
import os
import PIL.Image, PIL.ImageTk
from PyAutoClassroom import Student
from tkinter import *

root = Tk()

main_window_settings = {
    root.iconbitmap(file_path['CWD'] + '\\Photos\\icon.ico'),
    root.title('PyAutoClassroom'),
    root.geometry('500x500'),
    root.minsize(500,500),
    root.maxsize(500,500),
    # root.configure(background = '#24292e'),
}

photos = {
    'travis_scott' : PIL.ImageTk.PhotoImage(PIL.Image.open(file_path['CWD'] + '\\Photos\\travisscott.jpg').resize((200,200))),    
    'execute_code_image' : PIL.ImageTk.PhotoImage(PIL.Image.open(file_path['CWD'] + "\\Photos\\download.png").resize((40,40)))
}

def execute_code():
    pass

def add_to_queue():
    pass

def save_login_def():
    os.chdir(file_path['CWD'] + '\\data')
    if 'info.txt' not in os.listdir(file_path['CWD'] + '\\data'):
        with open('info.txt', 'x') as f:
            f.write(email_entry.get() + '\n' + password_entry.get())
    else:
        with open('info.txt', 'w') as j:
            j.write(email_entry.get() + '\n' + password_entry.get())


text_input = Entry(root, bd=2, width=50,)
text_input.place(
    relx=0.315,
    rely=0.0,
    anchor='n')
text_input.insert(0,'Enter your classes here:')


email_entry = Entry(root, width=24, bd=2)
email_entry.place(
    relx=0.159,
    rely=0.05,
    anchor="n")
email_entry.insert(0, 'Enter your email:')


password_entry = Entry(root,width=24, bd=2 )
password_entry.place(
    relx=0.472,
    rely=0.05,
    anchor="n")
password_entry.insert(0,'Enter your password:')


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

save_login_info = Button(root, text='Login', padx=13,pady=5, command=save_login_def)
save_login_info.place(
    relx=0.557,
    rely=0.2,
    anchor='center')

add_to_queue_button = Button(root, text='Save', padx=15, pady=5, relief='raised', command=add_to_queue)
add_to_queue_button.place(
    relx=0.557,
    rely=0.094,
    anchor='n')

# my_image = Label(root, padx=2+00, pady=200, image=photos['travis_scott'])
# my_image.place(
#     rely=0.37,
#     relx=0.3,
#     anchor='center')


root.mainloop()
