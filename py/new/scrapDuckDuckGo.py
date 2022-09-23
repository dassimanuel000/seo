from cgi import test
from pickle import TRUE
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
from deep_translator import GoogleTranslator

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

TAG_RE = re.compile(r'<[^>]+>')


def remove_tags(description):
    return TAG_RE.sub(' ', description)

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


binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
caps = DesiredCapabilities().FIREFOX
caps["marionette"] = True
driver = webdriver.Firefox(capabilities=caps, firefox_binary=binary, executable_path=r'C:\Python310\geckodriver.exe')
driver.get("https://google.com/")
time.sleep(3)

search = input("Entrer LE BONNE PHRASE CONSTRUITE AVEC VOTRE MOT CLE \n")
search = str(search)
search_translated = GoogleTranslator(source='auto', target='zh-CN').translate(search)
print(search_translated)

driver.get("https://duckduckgo.com/?q="+search_translated+"&ia=web")
time.sleep(2)
time.sleep(2)



def scrollweb():
    links = driver.find_element(By.XPATH, '//a[contains(@class, "result--more__btn")]')
    links.click()

    num1 = random.randint(1, 20)               #/html/body/div[2]/div[5]/div[3]/div/div[1]/div[5]/div[10]/article/div[1]/div/a
    print(num1)                                #/html/body/div[2]/div[5]/div[3]/div/div[1]/div[5]/div[2]/article/div[1]/div/a
    #try:                                       #/html/body/div[2]/div[5]/div[3]/div/div[1]/div[5]/div[10]/article/div[2]/h2/a
    #links = driver.find_element(By.XPATH, '//article[contains(@data-testid, "result")]//a[contains(@data-testid, "result-title-a")]')
                                           #/html/body/div[2]/div[5]/div[3]/div/div[1]/div[5]/div[16]/article/div[2]/h2/a
    try:
        links = driver.find_element(By.XPATH, '/html/body/div[2]/div[5]/div[3]/div/div[1]/div[5]/div['+str(num1)+']/article/div[2]/h2/a')
        step1 = links.get_attribute('href')
    except NoSuchElementException:
        links = driver.find_element(By.XPATH, '/html/body/div[2]/div[5]/div[3]/div/div[1]/div[5]/div['+str(num1)+']/article/div[1]/div/a')
        step1 = links.get_attribute('href')
        if len(step1) < 3 :
            scrollweb()
    print(step1)
    driver.get(step1)
    time.sleep(4)
    try:
        urla = driver.find_element(By.CLASS_NAME, "closeButton").click()
        for page_number in range(int(urla.split()[3])):
            time.sleep(2)
            urla.text
                #print(i.get_attribute("src"))
    except NoSuchElementException:
        print("Element is not present")
        
    time.sleep(2)
    try:
        urla = driver.find_element(By.CLASS_NAME, "Close").click()
        for page_number in range(int(urla.split()[3])):
            time.sleep(2)
            urla.text
                #print(i.get_attribute("src"))
    except NoSuchElementException:
        print("2 Element is not present")
        
        
    input('ereeeeeeeeeeeeeeeeeeeeeeeeeeeeee')

    try:
        article = driver.find_element(By.TAG_NAME, "article")
        eh1 = article.find_element(By.TAG_NAME, "h1")
        h1 = eh1.text
        if len(h1) > 0:
            print(" 1 il a un titre ")
            p = eh1.find_element(By.XPATH, '/following-sibling::p')
            #p = p.get_attribute("textContent")
            for i_p in p:
                paragraphe = (i_p.get_attribute('innerHTML'))
                paragraphe = remove_tags(paragraphe)
                print(paragraphe)
    except NoSuchElementException:
        try:
            eh1 = driver.find_element(By.TAG_NAME, "h1")
            h1 = driver.find_element(By.TAG_NAME, "h1").text
            if len(h1) > 0:
                print(" 2 il a un titre ")
                p =eh1.find_element(By.XPATH, '/following-sibling::p')
                #p = p.get_attribute("textContent")
                for i_p in p:
                    paragraphe = (i_p.get_attribute('innerHTML'))
                    paragraphe = remove_tags(paragraphe)
                    print(paragraphe)
                try:
                    h2 = driver.find_element(By.TAG_NAME, 'h2').text
                    if len(h2) > 0:
                        print(" 2.2 il a un titre ")
                except NoSuchElementException:
                    pass
        except NoSuchElementException:
            input('trouve une bonne page ')
            scrollweb()
            pass
        
    input('+-----------------------------------')

scrollweb()