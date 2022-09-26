from cgi import test
from pickle import TRUE
import random
from logging import exception
from selenium import webdriver
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
from googletrans import Translator
import urllib.request
import requests
# pour colorer les prints
import colorama
import os
import os.path
import re
import time
import json
import pymongo
import json

import docx
    
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

list_search = list()
my_list = list()

translator = Translator()

def function_for_page_per_page(url, times):
    driver.get(url)
    time.sleep(times)
    try:
        h1 = driver.find_element(By.TAG_NAME, "h1").text
        try:
            #translate_text = translator.translate('Hola mundo!', lang_src='es', lang_tgt='en')  
            translation = GoogleTranslator(source='auto', target='fr').translate(h1)
            #translation = translator.translate(h1, dest='fr')
            h1 = (translation)
            print(h1)
            #h1 = GoogleTranslator(source='auto', target='fr').translate(h1)
        except NoSuchElementException:
            time.sleep(6)
            h1 = "NULL"
        
        for k in h1.split("\n"):
            h1 = (re.sub(r"[^a-zA-Z0-9]+", ' ', k))
        smallH1 = h1.split(',', 1)[0] 
        filename = ''.join(e for e in smallH1 if e.isalnum())
        print(" Titre 1" +h1)
        try:
            new_dir = str(r"C:\Users\admin\Documents\DEV TEST\ucoz-seo\ "+str(filename))
        except NoSuchElementException:
            new_dir = str(r"C:\Users\admin\Documents\DEV TEST\ucoz-seo\error")
        
        print(new_dir)
        if not os.path.exists(new_dir):
            os.makedirs(new_dir) 
    
    except NoSuchElementException:
        function_for_page_per_page(url, times+3)
        
    try:
        first_phrase = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[2]/div/div[1]/div[2]/p").text
        
        try:
            first_phrase = GoogleTranslator(source='auto', target='fr').translate(first_phrase)
            #first_phrase = translator.translate(str(first_phrase), dest='fr')
        except NoSuchElementException:
            time.sleep(6)
            first_phrase = " Citation "
        print("1er Phrase " + str(first_phrase))
    except NoSuchElementException:
        first_phrase = "Description"
        print("1er Phrase " + str(first_phrase))
        
    title1 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-screen"]//h2/parent::*'))).text
    title1 = str(title1)
    try:
        title1 = GoogleTranslator(source='auto', target='fr').translate(title1)
        #title1 = translator.translate(str(title1), dest='fr')
    except NoSuchElementException:
        time.sleep(6)
        title1 = "DESCRIPTION"
    print(" Titre 2 " + str(title1))
    
    try:
        img_src = driver.find_element(By.XPATH, '(//*[@id="main-screen"]//img)[10]')
        src = img_src.get_attribute('src')
        r = requests.get(src)
        #filename = new_dir +"\ "+  smallH1 +" .png"
        filename = "./"+  smallH1 +".png"
        with open(filename, "wb") as f:
            f.write(r.content)
        print("image " + src)
    except NoSuchElementException:
        src = "none"
        print("image " + src)
    
    myDict = {}
    myDict["h1"] = str(h1)
    myDict["smallH1"] = str(smallH1)
    myDict["new_dir"] = str(new_dir)
    myDict["img"] = smallH1 +".png"
    myDict["first_phrase"] = str(first_phrase)
    myDict["title1"] = str(title1)
    list_search.append(myDict)


def scrollweb():
    
    doc = docx.Document('testchinfr.docx')
    for i in doc.paragraphs:
        line = i.text
        line = str(line)
        print(line.readlines())
        #print(i.text)
    """
    f = open('article.json')
    data = json.load(f)
    count=0
    for i in data:
        print(i)
        time.sleep(4)
        function_for_page_per_page(i, 4)
        count +=1
        if count  == 3:
            input("recommence")
            with open(f"content.json", "wb") as writeJSON:
                jsStr = json.dumps(list_search)
                # the decode() needed because we need to convert it to binary
                writeJSON.write(jsStr.encode('utf-8')) 
                print ('end')
    f.close()"""
    
    
"""
def scrollweb():
    driver.get('https://hahow.in/contents')
    time.sleep(4)
    
    for i in range(1, 2):
        driver.find_element(By.XPATH, '//button[contains(@data-testid, "loadMoreButton")]').click()
        time.sleep(3)                     #/html/body/div[1]/div/main/div[3]/div/section[2]/div/div[2]/a
    input('------------------------')
    count = 0
    
    links = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//a[@href]")))
    for link in links:
        vrailink = (link.get_attribute('href'))
        if 'contents/articles' in vrailink:
            my_list.append(vrailink)
            count = count+ 1
    
    print(count)
    print(my_list)
    with open(f"article.json", "wb") as writeJSON:
        jsStr = json.dumps(my_list)
        # the decode() needed because we need to convert it to binary
        writeJSON.write(jsStr.encode('utf-8')) 
        print ('end')
    for scrappingUrl in my_list:
        function_for_page_per_page(scrappingUrl, 5)
    
    with open(f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json", "wb") as writeJSON:
        jsStr = json.dumps(list_search)
        # the decode() needed because we need to convert it to binary
        writeJSON.write(jsStr.encode('utf-8')) 
        print ('end')
"""

scrollweb()
input('+++++++++++++++++++')