import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def get_current_end_point(url: str) -> str:
    return url.split("/")[-1]

def login (driver):
    
    print(f"[*] Login in as New user")
    num1 = random.randint(1, 1985)
    #download https://raw.githubusercontent.com/fredrikparkell/fredrikparkell.github.io/49f8f15c1573dce26f99c2e4d12b08ae7efdcbd0/fredrikparkell-dot-com/fm/create-random-player/names/Guadeloupe-lastnames.txt
    with open(r"/home/ds/Documents/WORK/TARGET-SEO/UCOZ-AVIS/lastnames.txt", 'r') as fp:
        x = fp.readlines()[num1]
        print(x)
    title = ''.join(str(sx) for sx in x)
    
    author = ""
    email = ""
    comment = ""
    input(title +'89899999999999999')
    driver.find_element(By.ID, 'fl-title').send_keys(title)
    driver.find_element(By.ID, 'password').send_keys(author)
    driver.find_element(By.ID, 'login-button').click()
    assert get_current_end_point(driver.current_url) == "inventory.html"


if __name__ == "__main__":
    print ('Starting the browser...')
    options = ChromeOptions()
    options.add_argument("--no-sandbox") 
    options.add_argument("--disable-dev-shm-usage") 
    options.add_argument("--headless") 
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")

    #driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    #print ('Browser started successfully. Navigating to the demo page to login.')
    #time.sleep(5)
    login(driver)
    #driver.get('https://ucoz.fr/avis/trouver-un-therapeute-avis/')