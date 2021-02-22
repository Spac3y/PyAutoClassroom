import os
from shutil import move

file_path = {
    'APPDATA' : os.getenv("LOCALAPPDATA"),
    'ROAMING' : os.getenv("ROAMING"),
    'DESKTOP' : os.getenv('USERPROFILE') + '\\Desktop',
    'CWD': os.getcwd(),
    }

def move_chromedriver():
    os.chdir(file_path["DESKTOP"])
    if 'chromedriver.exe' in os.listdir():
        try:
            move(file_path['DESKTOP'] + '\\chromedriver.exe', file_path['CWD'])
        except FileNotFoundError:
            print(0)
    else:
        print('File Not Found')

