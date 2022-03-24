from datetime import datetime
import json
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import time


class Student:
    def __init__(self,email,password, maximize_window = False):
        self.email = email
        self.password = password
        chrome_Options = Options()
        chrome_Options.add_argument("--use-fake-ui-for-media-stream")
        self.path = os.getcwd()
        self.driver = webdriver.Chrome(
            self.path.replace('lib', '') + '\\chromedriver.exe', chrome_options=chrome_Options)
        self.wait = WebDriverWait(self.driver, 30)
        if maximize_window:
            self.driver.maximize_window()
        with open(self.path + '\\lib\\data\\classes.json' ,'r') as f:
            data = json.load(f)

            
    def login(self):
        self.driver.get('https://stackoverflow.com/')
        #Navigate through StackOverflow
        login = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/header/div/ol[2]/li[2]/a[2]"))
            )
        login.click()
        #Navigate through StackOverflow
        login = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"openid-buttons\"]/button[1]"))
            )
        login.click()
        #Send email to google login page
        login = self.wait.until(
            EC.presence_of_element_located((By.ID,'identifierId'))
            )
        login.send_keys(self.email)
        #Click "next" button in google login page
        login = self.wait.until(
            EC.presence_of_element_located((By.ID,'identifierNext'))
            )
        login.click()
        time.sleep(1.5)
        #Send password to google login page
        login = self.wait.until(
            EC.presence_of_element_located((By.XPATH,"//input[@class='whsOnd zHQkBf']"))
            )
        login.send_keys(self.password)
        #Click "next" button in google login page
        login = self.wait.until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="passwordNext"]/div/button'))
            )
        login.click()

        del login
        print(f'[{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}] Logged in as {self.email}')

    def check_homework(self):
        self.driver.get('https://classroom.google.com/h')
        all_hmrks = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, '//a[@class = "onkcGd zZN2Lb-Wvd9Cc VBEdtc-Wvd9Cc apFsO"]'))
            )
        hmrk_list = []
        for p in all_hmrks:
            hmrk_list.append(p.text)
        if len(hmrk_list) == 0:
            print("You don't have any homework!")
        else:
            for i in hmrk_list:
                print(i)

    def enter_course(self, class_name =None, enter_time = 00, check_if_person_present = True):
        # has_gotten_error = False
        self.driver.get('https://classroom.google.com/u/0/h')

        classes = self.wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@class = 'YVvGBb csjh4b']"))
            )
        for clss in classes:
            if str(clss.text.lower()) == str(class_name.lower()):
                time.sleep(0.5)
                clss.click()

        #Get the current google meet link
        try:
            link = self.wait.until(
                EC.presence_of_element_located((By.XPATH,'//*[@id="yDmH0d"]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/span/a/div'))
                ).text
            self.driver.get(link)

        except TimeoutException:
            print(
                f'\n[{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}]No link provided...')
            return 0
            
        #Decline Microphone
        button = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div/span/span/div/div[1]'))
            )
        button.click()
        #Decline Video
        button = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div/span/span/div/div'))
            )
        button.click()

        while datetime.now().minute != enter_time or datetime.now().minute > enter_time+10:
            time.sleep(60)
            print(
                f'[{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}]Waiting.....')

        print(
            f"[{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}]Entering.....\n")

        if check_if_person_present:
            time.sleep(2)
            is_active = self.driver.find_element_by_xpath(
                '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[2]').text
            while is_active.upper() == "NO ONE ELSE IS HERE":
                print(f'[{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}]No one else is here right now')
                self.driver.navigate().refresh()
                time.sleep(5)

        #Join Now button
        button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span'))
            )
        button.click()
         
        del button,check_if_person_present,is_active,is_active
    
    def first_setup(self):
        got_error = False
        class_list = []
        self.driver.get("https://classroom.google.com")
        classes = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class = 'YVvGBb csjh4b']"))
            )
        for clas in classes:
            class_list.append(clas.text)
        i = 0 
        for clas in classes:
            got_error = False
            if clas.text == class_list[i]:
                current_class = clas.text
                clas.click()
                try:
                    self.WebDriverWait(self.driver, 3).until(
                        EC.presence_of_element_located((By.CLASS_NAME,'VkMwfe'))
                        )
                except TimeoutException:
                    class_list.remove(current_class)
                self.driver.back()
                self.WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'YVvGBb csjh4b'))
                    )
                i += 1
        with open(self.path + "/data/classes.json") as f:
            json.dump(class_list, f)
        self.driver.quit()
        del got_error, class_list

    def __exit__(self, exit_time=40):
        while datetime.now().minute < exit_time:
            time.sleep(60)

        self.driver.get("https://classroom.google.com/u/0/h")
        print(
            f'[{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}] Done with this class!....')
    
    def __quit__(self):
        print(
            f'[{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}] Quitting!')
        self.driver.quit()
        
    
def main():
   Vlad = Student("vlad.gavanescu@cnodobescu.ro", "Vlad2020", False)
   Vlad.login()
   Vlad.enter_course('TIC', 43, False)

if __name__ == '__main__':
    main()