from cgi import test
import email
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
driver.get("https://ucoz.fr/wp-admin/")
wait = WebDriverWait(driver, 60)
# connection au compte wp-admin
driver.find_element(By.XPATH,'//*[@id="user_login"]').send_keys('ucoz.avis@gmail.com')
driver.find_element(By.XPATH,'//*[@id="user_pass"]').send_keys('pD7C38hWw')

# collection des xPath important
xPathLogin= '//*[@id="wp-submit"]'
# try: 
#     xPathAvis = '/html/body/div[1]/div[1]/div[2]/ul/li[6]/a/div[3]'
# except NoSuchElementException:
#     driver.get('https://ucoz.fr/wp-admin/edit.php?post_type=places')
# else:
#     xPathAvis = '/html/body/div[1]/div[1]/div[2]/ul/li[6]/a/div[3]'
urlXPathAvis = 'edit.php?post_type=places'
xPathAvis = '//a[@href="'+urlXPathAvis+'"]'
classNameAvis = 'wp-menu-name'
urlXpathAddAvis = 'https://ucoz.fr/wp-admin/post-new.php?post_type=places'
xPathAddAvis = '//a[@href="'+urlXpathAddAvis+'"]'
xPathAllCat = '//*[@id="places-category-all"]'

# remplissage des informations
idPermaLink = 'custom-permalinks-post-slug'
idTitle = 'title'
idDescription = 'content'
idPhone = 'acf-field_5ed556f24asdwd'
idEmail = 'acf-field_5edascaf24aacwd'
idWebsite = 'acf-field_5edascaf24asdwd'
idRequeteCible = 'focus-keyword-input-metabox'
idSlug = 'yoast-google-preview-slug-metabox'
idToGetText = 'content-html'
# xPathMetaDescription = '/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/div/div/div[3]/div[1]/div[3]/div[2]/div/div[2]/div/div[4]/div/div/section/div/section[2]/div[4]/div[2]'
idMetaDescription = 'yoast-google-preview-description-metabox'
# classMetaDescription = 'DraftEditor-root'

waitBeforeClickOnXpath(xPathLogin)
time.sleep(2)

my_list = list()
final_result = list()

print('------------------------------------------------------------------------------------------')
#for i in range(16):
for i in range(15,0,-1):
    time.sleep(4)
    print(i)
    driver.get("https://ucoz.fr/wp-admin/edit.php?post_type=places&paged="+str(i)+"")
    #links = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[1]/div[4]/form[1]/table/tbody/tr/td[1]/strong/a')
    #count = (len(links))                    
    links = driver.find_elements(By.CLASS_NAME,'row-title')
    count = len(links)
    if count < 4:
        time.sleep(1)
        links = driver.find_elements(By.CLASS_NAME,'row-title')
        count = len(links)
        print(count)
    else:
        print(count)
    #links = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[1]/div[4]/form[1]/table/tbody/tr['+ str(i) +']/td[1]/strong/a')
    for i in links:
        step1 = (i.get_attribute('href'))
        my_list.append(step1)
    #for increment in range(1, count):
    for j in my_list:
        print(j)
        time.sleep(5)
        driver.get(j)
        try:
            title = driver.find_element(By.XPATH, '//*[@id="title"]')
            title= title.get_attribute('value')
        except NoSuchElementException:
            input('une erreur cette avis')
        print('titre ==='+title)
        try:
            _schema_audio_object_name = driver.find_element(By.XPATH, '//*[@id="_schema_audio_object_name"]')
            _schema_audio_object_name.clear()
            _schema_audio_object_name.send_keys('Top des Avis '+ title)
            _schema_audio_object_upload_date = driver.find_element(By.XPATH, '//*[@id="_schema_audio_object_upload_date"]')
            _schema_audio_object_upload_date.clear()
            _schema_audio_object_upload_date.send_keys('2022-09-12')
            _schema_audio_object_duration = driver.find_element(By.XPATH, '//*[@id="_schema_audio_object_duration"]')
            _schema_audio_object_duration.clear()
            _schema_audio_object_duration.send_keys('PT1H'+str(random.randint(0, 60))+'M')
            _schema_audio_object_description = driver.find_element(By.XPATH, '//*[@id="_schema_audio_object_description"]')
            _schema_audio_object_description.clear()
            _schema_audio_object_description.send_keys(title +' Publiez des avis, Lisez des avis, renseignez-vous!')
        except NoSuchElementException:
            input('une erreur cette avis')
        time.sleep(2)
        try:
            _schema_review_rating = driver.find_element(By.XPATH, '//*[@id="_schema_review_rating"]')
            _schema_review_rating.clear()
            _schema_review_rating.send_keys('4')
            _schema_review_name = driver.find_element(By.XPATH, '//*[@id="_schema_review_name"]')
            _schema_review_name.clear()
            _schema_review_name.send_keys(title)
        except NoSuchElementException: 
            input('une erreur cette avis')
        time.sleep(2)
        try:
            item_jsonld = driver.find_element(By.XPATH, '//*[@id="sq-nav-item_jsonld"]')
            item_jsonld.click()
            time.sleep(1)                                
            reviewclick = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div[4]/form/div/div/div[3]/div[1]/div[8]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div[2]/select/option[8]')                  
            #reviewclick.send_keys(Keys.COMMAND) 
            reviewclick.click()
            """ActionChains(driver) \
                .key_down(Keys.CONTROL) \
                .click(reviewclick) \
                .key_up(Keys.CONTROL) \
                .perform()"""
            reviewclickone = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div[4]/form/div/div/div[3]/div[1]/div[8]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div[2]/select/option[12]')
            reviewclickone.send_keys(Keys.COMMAND) 
            reviewclickone.click()
            """ActionChains(driver) \
                .key_down(Keys.CONTROL) \
                .click(reviewclickone) \
                .key_up(Keys.CONTROL) \
                .perform()"""
        except NoSuchElementException: 
            input('une erreur cette avis')
            
        try:
            _schema_sameAs = driver.find_element(By.XPATH, '//*[@id="_schema_sameAs"]')
            _schema_sameAs.clear()
            _schema_sameAs.send_keys('https://www.facebook.com/Trouver-des-avis-110105471844952\nhttps://www.youtube.com/channel/UC1FoNUXzB2vBKqqwjw_Lsxw\nhttps://www.linkedin.com/in/ucoz-avis-209b8924b/\nhttps://www.pinterest.fr/ucozavis/')
        except NoSuchElementException: 
            input('une erreur cette avis')

        saveButton = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div[4]/form/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/a')
        saveButtonTo = saveButton.send_keys(Keys.TAB)
        action = ActionChains(saveButtonTo)
        time.sleep(1)
        saveButton = driver.find_element(By.XPATH, '//*[@id="publish"]')
        saveButton.send_keys(Keys.ENTER)
        final_result.append(j)
driver.close()


with open("done.json", "wb") as writeJSON:
   jsStr = json.dumps(final_result)
   # the decode() needed because we need to convert it to binary
   writeJSON.write(jsStr.encode('utf-8')) 
print ('end')