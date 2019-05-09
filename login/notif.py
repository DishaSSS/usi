import sqlite3
from threading import Timer
from time import sleep
import os
from selenium import webdriver
from bs4 import BeautifulSoup
import selenium.webdriver.support.expected_conditions as EC

path=os.path.dirname(os.path.realpath(__file__))+'/chromedriver'

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

def check():
    db = sqlite3.connect('../db.sqlite3')

    cursor = db.cursor().execute("SELECT mood_reg, mood_passw from LOGIN_USER")
    users = cursor.fetchall()
    for user in users[2:]:
            username = user[0]
            password = user[1]
            opt = webdriver.ChromeOptions()
            opt.add_argument("--incognito")
            opt.add_argument("--headless")
            driver = webdriver.Chrome(executable_path=path,options=opt)
            try:
            	driver.get('http://moodle.vitbhopal.ac.in/login/index.php')

            	url= driver.current_url
            	driver.find_element_by_name('username').send_keys(username)
            	driver.find_element_by_name('password').send_keys(password)
            	driver.find_element_by_id('loginbtn').click()
            except:
            	driver.refresh()
            	url= driver.current_url
            	driver.find_element_by_name('username').send_keys(username)
            	driver.find_element_by_name('password').send_keys(password)
            	driver.find_element_by_id('loginbtn').click()
            sleep(5)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            notif = soup.findAll('div',{'id':'nav-notification-popover-container'})[0]
            message = soup.findAll('div',{'id':'nav-message-popover-container'})[0]
            show1 = ""
            show2 = ""
            print(notif.findAll('div',{'class':'count-container'}))
            if notif.findAll('div',{'class':'count-container'})[0].text=="" :
                show1="0"
            else:
                show1=notif.findAll('div',{'class':'count-container'})[0].text
            if message.findAll('div',{'class':'count-container'})[0].text == "":
                show2="0"
            else:
                show2=message.findAll('div',{'class':'count-container'})[0].text
            print("Messages : ", show2)
            print("Notifications: ", show1)
            driver.close()
x = RepeatedTimer(10,check)
try:
    sleep(5)
except:
    pass
