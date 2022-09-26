from cgi import test
import random
from logging import exception
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import InvalidSelectorException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from datetime import datetime
from os.path import exists
# pour colorer les prints
from colorama import Fore
from colorama import Style
from urllib.parse import ParseResult, urlparse

# pour colorer les prints
import colorama
import os
import os.path
import re
import time
import json
import pymongo
import json

from pymongo import MongoClient
from pprint import pprint

def scroll_function(i):
    height = i * 1000
    time.sleep(1.3)
    driver.execute_script("window.scrollTo("+ str(height) +", "+ str(height) +")")
    time.sleep(1.3)
    
# fonction pour donner du délai et cliquer les xpath
def waitBeforeClickOnXpath(xPath):
    time.sleep(1)
    print("clicking on " + xPath + "...")
    button = driver.find_element(By.XPATH, xPath)
    driver.execute_script("arguments[0].click();", button)
    time.sleep(1)
    print("Continue the script")

def waitBeforeClickOnClass(className):
    print("waiting page loading")
    time.sleep(3)
    print("clicking on " + className + "...")
    button = driver.find_element(By.CLASS_NAME, className)
    driver.execute_script("arguments[0].click();", button)
    print("button clicked")
    print("now waiting server response..")
    time.sleep(3)
    print("Continue the script")

def waitBeforeClickOnId(id):
    print("waiting page loading")
    time.sleep(3)
    print("clicking on " + id + "...")
    button = driver.find_element(By.ID, id)
    driver.execute_script("arguments[0].click();", button)
    print("button clicked")
    print("now waiting server response..")
    time.sleep(3)
    print("Continue the script")

# rempli de texte la case formulaire avec l'id correspondant
def fillById(id, filler):
    print("waiting page loading")
    time.sleep(3)
    driver.find_element(By.ID, id).send_keys(filler)
    print("form filled")
    print("now waiting server response..")
    time.sleep(3)
    print("Continue the script")

def fillByIdWithSteps(id ,filler):
    print("waiting page loading")
    time.sleep(3)
    driver.find_element(By.ID, id).send_keys(Keys.CONTROL + "a")
    print("Taking all that already exist")
    time.sleep(1)
    driver.find_element(By.ID, id).send_keys(Keys.DELETE)
    print("Cleaning")
    time.sleep(1)
    driver.find_element(By.ID, id).send_keys(filler)
    print("Fill with our value")
    time.sleep(1)
    print("Complete")
    print("now waiting server response..")
    time.sleep(3)
    print("Continue the script")

def fillByClass(clss ,filler):
    print("waiting page loading")
    time.sleep(3)
    element = driver.find_element_by_class_name(clss).click()
    time.sleep(1)
    element.send_keys(filler)
    print("Fill with our value")
    time.sleep(1)
    print("Complete")
    print("now waiting server response..")
    time.sleep(3)
    print("Continue the script")

def fillByXpath(xpath, filler):
    print("waiting page loading")
    time.sleep(3)
    driver.find_element(By.XPATH, xpath).send_keys(filler)
    print("form filled")
    print("now waiting server response..")
    time.sleep(3)
    print("Continue the script")

def tryAndRetryClickXpath(xPath):
    try : 
        waitBeforeClickOnXpath(xPath)
    except NoSuchElementException:
        print("the element needs to be charged...")
        time.sleep(10)
        waitBeforeClickOnXpath(xPath)

def tryAndRetryClickClassName(class_name):
    try : 
        waitBeforeClickOnClass(class_name)
    except NoSuchElementException:
        print("the element needs to be charged...")
        time.sleep(10)
        waitBeforeClickOnClass(class_name)

def tryAndRetryClickID(id):
    try : 
        waitBeforeClickOnClass(id)
    except NoSuchElementException:
        print("the element needs to be charged...")
        time.sleep(10)
        waitBeforeClickOnClass(id)


def tryAndRetryFillById(id, value):
    try:
        fillById(id, value)
    except NoSuchElementException:
        print("the element needs to be charged...")
        time.sleep(10)
        fillById(id, value)

def tryAndRetryFillByIdWithSteps(idStep1, id, value):
    try:
        button = driver.find_element(By.ID, idStep1)
        driver.execute_script("arguments[0].click();", button)
        fillById(id, value)
    except NoSuchElementException:
        button = driver.find_element(By.ID, idStep1)
        driver.execute_script("arguments[0].click();", button)
        print("the element needs to be charged...")
        time.sleep(10)
        fillById(id, value)
    except ElementNotInteractableException:
        button = driver.find_element(By.ID, idStep1)
        driver.execute_script("arguments[0].click();", button)
        print("the element needs to be charged...")
        time.sleep(10)
        fillById(id, value)

def writeLetterByLetterId(id, word):
    print("waiting page loading")
    time.sleep(3)
    driver.find_element(By.ID, id).send_keys(Keys.CONTROL + "a")
    print("Taking all that already exist")
    time.sleep(1)
    driver.find_element(By.ID, id).send_keys(Keys.DELETE)
    print("Cleaning")
    for i in word:
        driver.find_element(By.ID, id).send_keys(i)

def tryAndRetryFillByIdWithExtraSteps(idStep1, id, value):
    try:
        button = driver.find_element(By.ID, idStep1)
        driver.execute_script("arguments[0].click();", button)
        writeLetterByLetterId(id, value)
    except NoSuchElementException:
        button = driver.find_element(By.ID, idStep1)
        driver.execute_script("arguments[0].click();", button)
        print("the element needs to be charged...")
        time.sleep(10)
        writeLetterByLetterId(id, value)
    except ElementNotInteractableException:
        button = driver.find_element(By.ID, idStep1)
        driver.execute_script("arguments[0].click();", button)
        print("the element needs to be charged...")
        time.sleep(10)
        writeLetterByLetterId(id, value)

binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
caps = DesiredCapabilities().FIREFOX
caps["marionette"] = True
driver = webdriver.Firefox(capabilities=caps, firefox_binary=binary, executable_path=r'C:\Python310\geckodriver.exe')
driver.get("https://google.com/")
time.sleep(3)

cookieGoogle = driver.find_element(By.ID, 'L2AGLb').click()

author = ""
e_mail = ""
comment =""

def avis_therapeute(author, e_mail,comment):
    num1 = random.randint(1, 20)
    driver.get("https://fr.trustpilot.com/categories/health_medical?page="+str(num1)+"")
    try:
        time.sleep(5)
        driver.find_element(By.ID, 'onetrust-reject-all-handler').click()
        time.sleep(2)
    except NoSuchElementException:
        driver.get("https://fr.trustpilot.com/categories/health_medical?page="+str(num1)+"")
        time.sleep(5)
        
    num1 = random.randint(1, 15)
    
    try:                                      #/html/body/div[1]/div/div/main/div/div[2]/div/section/div[10]/a
        links = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div/div[2]/section/div[2]/div[2]/div['+str(num1)+']/a')
        step1 = (links.get_attribute('href'))
    except NoSuchElementException:             #/html/body/div[1]/div/div/main/div/div[2]/div/section/div[23]/a
        links = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div/div[2]/div/section/div['+str(num1)+']/a')
        step1 = (links.get_attribute('href'))
    
    driver.get(step1)
    time.sleep(4)
    driver.find_element(By.ID, 'star-filter-page-filter-five').click()
    time.sleep(12)
             
    num1 = random.randint(6, 24)
    try:
        author = " "                   
        author = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div/div[4]/section/div['+str(num1)+']/article/aside/div/a/span')
        author = (author.get_attribute('innerHTML'))
    except NoSuchElementException:  #spelling error making this code not work as expected
        avis_therapeute(author, e_mail,comment)
    print(author)
    
    try:
        title = " "
        title = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div/div[4]/section/div['+str(num1)+']/article/section/div[2]/a/h2')
        title = (title.get_attribute('innerHTML'))
    except NoSuchElementException:  #spelling error making this code not work as expected
        avis_therapeute(author, e_mail,comment)
    print(title)

    try:
        comment = " "
        comment = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div/div[4]/section/div['+str(num1)+']/article/section/div[2]/p[1]')
        comment = (comment.get_attribute('innerHTML'))
    except NoSuchElementException:  #spelling error making this code not work as expected
        avis_therapeute(author, e_mail,comment)
    print(comment)
    
    driver.get("https://ucoz.fr/avis/trouver-un-therapeute-avis/")
    time.sleep(9)
    wait = WebDriverWait(driver, 60)
    # connection au compte wp-admin
    """driver.find_element(By.XPATH,'//*[@id="user_login"]').send_keys('ucoz.avis@gmail.com')
    num1 = random.randint(1, 1985)
    #download https://raw.githubusercontent.com/fredrikparkell/fredrikparkell.github.io/49f8f15c1573dce26f99c2e4d12b08ae7efdcbd0/fredrikparkell-dot-com/fm/create-random-player/names/Guadeloupe-lastnames.txt
    with open(r"C:\Python310\lastnames.txt", 'r') as fp:
        x = fp.readlines()[num1]
        print(x)
    author = ''.join(str(sx) for sx in x)"""
    
    e_mail = author.replace(" ", "")
    e_mail = re.sub('[^A-Za-z0-9]+', '', e_mail)
    e_mail = e_mail + "@gmail.com"
    
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[2]/div[2]/div/form/div[8]/p/span/a[5]').click()
    driver.find_element(By.ID, 'fl-title').send_keys(title)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[2]/div[2]/div/form/div[1]/input').send_keys(author)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[2]/div[2]/div/form/div[2]/input').send_keys(e_mail)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[2]/div[2]/div/form/div[3]/textarea').send_keys(comment)
    
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[2]/div[2]/div/form/div[4]/button').click()
    time.sleep(5)
    driver.get("https://ucoz.fr/trouver-un-therapeute-avis/")
    time.sleep(9)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div[1]/div[3]/div/div/div/form/div[1]/input').send_keys(author)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div[1]/div[3]/div/div/div/form/div[2]/input').send_keys(e_mail)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div[1]/div[3]/div/div/div/form/div[3]/textarea').send_keys(comment)
    
    driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div[1]/div[3]/div/div/div/form/div[4]/button').click()
    time.sleep(5)
    driver.get("https://ucoz.fr/trouver-un-expert/")
    time.sleep(9)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div[1]/div[3]/div/div/div/form/div[1]/input').send_keys(author)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div[1]/div[3]/div/div/div/form/div[2]/input').send_keys(e_mail)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div[1]/div[3]/div/div/div/form/div[3]/textarea').send_keys(comment)
    
    driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div[1]/div[3]/div/div/div/form/div[4]/button').click()
    time.sleep(6)
    driver.get("https://ucoz.fr/quel-site-internet-pour-trouver-un-therapeute/")
    time.sleep(9)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div[1]/div[2]/div/div/div/form/div[1]/input').send_keys(author)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div[1]/div[2]/div/div/div/form/div[2]/input').send_keys(e_mail)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div[1]/div[2]/div/div/div/form/div[3]/textarea').send_keys(comment)
    
    driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div[1]/div[2]/div/div/div/form/div[4]/button').click()
    time.sleep(6)
    
    
    driver.get("https://trouver-un-therapeute.fr/therapeute/")
    time.sleep(9)
    driver.find_element(By.XPATH, '//*[@id="inputName"]').send_keys(author)
    driver.find_element(By.XPATH, '//*[@id="inputEmail"]').send_keys(e_mail)
    driver.find_element(By.XPATH, '//*[@id="inputComments"]').send_keys(comment)
    
    driver.find_element(By.XPATH, '//*[@id="submit"]').click()
    
    
avis_therapeute(author, e_mail,comment)
time.sleep(5)


