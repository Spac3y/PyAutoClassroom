from datetime import datetime
from file_mover import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

class Student:
    def __init__(self,email,password, maximize_window = False):
        self.email = email
        self.password = password
        chrome_Options = Options()
        chrome_Options.add_argument("--use-fake-ui-for-media-stream")
        self.driver = webdriver.Chrome(
           str(file_path['CWD'])+'\\chromedriver.exe' , chrome_options=chrome_Options)
        if maximize_window:
            self.driver.maximize_window()
        else:
            pass
            
    def wait_n_click(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except:
            #print(
            #    f'[{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}]' + '!')
            time.sleep(2)
            self.wait_n_click(xpath)

    def login(self):
        self.driver.get('https://stackoverflow.com/')

        self.driver.find_element_by_xpath(
            "/html/body/header/div/ol[2]/li[2]/a[2]").click()
        self.driver.find_element_by_xpath(
            "//*[@id=\"openid-buttons\"]/button[1]").click()
            

        email_box = self.driver.find_element_by_id('identifierId')
        email_box.send_keys(self.email)
        
        next_button_email = self.driver.find_element_by_id('identifierNext')
        next_button_email.click()

        time.sleep(2)

        pass_box = self.driver.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
        pass_box.send_keys(self.password)

        next_button_pass = self.driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button')
        next_button_pass.click()

        print(f'[{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}] Logged in as {self.email}')
        time.sleep(2)

    def check_homework(self):
        self.driver.get('https://classroom.google.com/h')
        time.sleep(6)
        all_hmrks = self.driver.find_elements_by_xpath('//a[@class = "onkcGd zZN2Lb-Wvd9Cc VBEdtc-Wvd9Cc apFsO"]')
        hmrk_list = []
        for p in all_hmrks:
            hmrk_list.append(p.text)
        if len(hmrk_list) == 0:
            print("You don't have any homework!")
        else:
            for i in hmrk_list:
                print(i)

    def enter_course(self, class_name =None, enter_time = 00, check_if_person_present = True):

        has_gotten_error = False
        self.driver.get('https://classroom.google.com/u/0/h')
        time.sleep(5)
        
        classes = self.driver.find_elements_by_xpath("//div[@class = 'YVvGBb csjh4b']")
        for clss in classes:
            if str(clss.text.lower()) == str(class_name.lower()):
                time.sleep(2)
                clss.click()
                #print('I found these classes ' + clss.text.lower())
        
        try:
            time.sleep(2)
            link = self.driver.find_element_by_xpath(
                '//*[@id="yDmH0d"]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/span/a/div').text
            self.driver.get(link)

        except NoSuchElementException:
            has_gotten_error = True
            print(
                f'\n[{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}]No link provided...')

        time.sleep(5)

        if has_gotten_error:
            return
            
        #Decline Microphone
        self.driver.find_element_by_xpath(
            '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div/span/span/div/div[1]').click()
        #Decline Video
        self.driver.find_element_by_xpath(
            '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div/span/span/div/div').click()

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
            while is_active.upper() == "No one else is here".upper():
                print(f'[{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}]Noone else is here right now')
                self.driver.navigate().refresh()
                time.sleep(5)

        #Join Now button
        self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span').click()

    def exit_course(self, exit_time = 40):
        while datetime.now().minute < exit_time:
            time.sleep(60)
        
        self.driver.get("https://classroom.google.com/u/0/h")
        print(
                f'[{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}] Done with this class!....')

    def exiting(self):
        print(
            f'[{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}] Exiting!')
        self.driver.quit()