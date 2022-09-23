import importlib.util

importlib.util.module_for_loader
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
options = Options()
options.add_argument("--disable-notifications")
try:
    from headers.headerSelenium import *
except ModuleNotFoundError:
    importlib.util.module_for_loader
    
try:
    from headers.headerSeleniumPoster import *
except ModuleNotFoundError:
    importlib.util.module_for_loader
    
try:
    from headers.headerPyMonGo import *
except ModuleNotFoundError:
    importlib.util.module_for_loader
    

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.cache.disk.enable", False)
profile.set_preference("browser.cache.memory.enable", False)
profile.set_preference("browser.cache.offline.enable", False)
profile.set_preference("network.http.use-cache", False) 
driver = webdriver.Firefox(options=options, firefox_profile=profile)
driver.get("https://trouver-un-candidat.com/wp-admin")
driver.maximize_window()
idLogin = 'user_login'
login = 'annoncetrouveruncandidat'
tryAndRetryFillById(driver, idLogin, login)
del idLogin, login

idMdp = 'user_pass'
mdp = '(%)Sku&mv#35OewiC%'
tryAndRetryFillById(driver, idMdp, mdp)
del idMdp, mdp

idSubmit = 'wp-submit'
waitBeforeClickOnId(driver, idSubmit)
del idSubmit

# len(cleanerDict["id"]

while i < len(10):
    
    driver.get('https://trouver-un-candidat.com/wp-admin/post-new.php?post_type=job_listing')

    time.sleep(5)

    # retrait de la pop up
    if i == 0:
        try:
            xPathPopUp = '//div[contains(@class,"components-modal__header")]//button[@aria-label="Fermez la boite de dialogue"]'
            tryAndRetryClickXpath(driver, xPathPopUp)
        except:
            time.sleep(5)
            xPathPopUp = '//div[contains(@class,"components-modal__header")]//button[@aria-label="Fermez la boite de dialogue"]'
            tryAndRetryClickXpath(driver, xPathPopUp)

    # récupération élément et affichage du titre
    now = datetime.now()
    current_time = now.strftime("%H %M%S")
    
    tryAndRetryFillByXpath(driver, xPathTitle, titre)

    # clique sur l'onglet emploi
    try:
        xpathEmploi = '/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div[2]/div[3]/div/div[2]/ul/li[1]/button'
        tryAndRetryClickXpath(driver, xpathEmploi)
    except NoSuchElementException:
        pass


    # envoie du texte dans la description du post
    xPathPlusTexte = '/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div/div/div/button'
    tryAndRetryClickXpath(driver, xPathPlusTexte)
    xPathParagraphe = "//button[contains(@class,'components-button block-editor-block-types-list__item editor-block-list-item-paragraph')]"
    tryAndRetryClickXpath(driver, xPathParagraphe)
    xPathDescription = "//p[contains(@class,'block-editor-rich-text__editable block-editor-block-list__block wp-block is-selected wp-block-paragraph rich-text')]"
    descriptionRobot = str(remove_tags('zefzfz'))
    driver.find_element(By.XPATH, xPathDescription).send_keys(descriptionRobot)
    time.sleep(5)

    # envoie du texte pour un lien externe
    xPathElementToScroll = '/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div[2]/div[2]'
    tryAndRetryClickXpath(driver, xPathElementToScroll)
    n = 11
    actions = ActionChains(driver) 
    actions.send_keys(Keys.TAB * n)
    actions.perform()
    print(Fore.RED + 'press tab complete' + Style.RESET_ALL)
    # time.sleep(10)
    
    actions.send_keys(Keys.ENTER)
    actions.perform()
    print(Fore.YELLOW + 'press enter complete' + Style.RESET_ALL)
    # time.sleep(10)
    
    actions.send_keys(Keys.ARROW_DOWN)
    actions.perform()
    print(Fore.BLUE + 'press down complete' + Style.RESET_ALL)
    # time.sleep(10)
    
    actions.send_keys(Keys.ENTER)
    actions.perform()
    print(Fore.YELLOW + 'press enter complete' + Style.RESET_ALL)
    # time.sleep(10)

    xPathUrlExt = '//*[@id="_job_apply_url"]'
    driver.find_element(By.XPATH, xPathUrlExt).send_keys(cleanerDict["url"][i])

    # Validation du poste
    time.sleep(10)
    xPathValidationPoste = '/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div[1]/div/div[3]/button[2]'
    tryAndRetryClickXpath(driver, xPathValidationPoste)
    
    # commenté cette ligne si y'a bug
    # time.sleep(15)
    # waitBeforeClickOnXpath(driver, xPathValidationPoste)
    try:
        waitBeforeClickOnXpath(driver, xPathValidationPoste)
    except:
        pass
    
    xPathConfirmation = '/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/button'
    tryAndRetryClickXpath(driver, xPathConfirmation)
    i = i + 1

driver.delete_all_cookies()
driver.quit()

del driver, options
