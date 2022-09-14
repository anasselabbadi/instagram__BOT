import selenium
import pyautogui
import sys
from time import sleep

def opening_instagram():
    import selenium
    from selenium import webdriver        
    path="C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://www.instagram.com/")
    

def WebDriverWait ():
    import selenium
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    element = WebDriverWait(driver,10).until(
        EC.persence_of_element_located((By.ID,"mount_0_0_XJ"))
        )
    
def searching_for_hashtags(Hashtags):
    import selenium
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    element = WebDriverWait(driver,10).until(
        EC.persence_of_element_located((By.ID,'//*[@id="mount_0_0_rX"]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/input'))
        )
    element = driver.find_element(By.XPATH, '//*[@id="mount_0_0_rX"]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/input')
    element.clear()
    element.send_keys(Hashtags)
    time.sleep(5)
    element.send_keys(Keys.RETURN)
    time.sleep(1)
    element.send_keys(Keys.RETURN)
def WebPageWait():
    import selenium
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    element = WebDriverWait(driver,10).until(
        EC.persence_of_element_located((By.ID,"mount_0_0_rm"))
        )
def find_Acc_and_follow(word):
    import selenium
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    file = open("instagramAcc.txt", "x")
    element1 = driver.find_element(By.XPATH, '//*[@id="mount_0_0_rm"]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div[1]/div[2]')
    element1.send_keys(Keys.RETURN)
    element2 = driver.find_element(By.XPATH, '//*[@id="mount_0_0_rm"]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button/div/div')
    element2.send_keys(Keys.RETURN)
    for i in range (0,101):
       element1 = driver.find_element(By.XPATH, '//*[@id="mount_0_0_rm"]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button')
       element1.click()
       element = driver.find_element(By.XPATH, '//*[@id="mount_0_0_rm"]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button/div/div')
       element.send_keys(Keys.RETURN)
       the_url = driver.find_element(By.XPATH, '//*[@id="mount_0_0_rm"]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div/div/div/div/span/a')
       f = open("instagramAcc.txt", "w")
       txt = the_url.get_attribute("href")
       f.write("https://www.instagram.com/"+txt)
       time.sleep(2)
    element3 = driver.find_element(By.XPATH, '//*[@id="mount_0_0_rm"]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div')
    element3.click()
    file = open("instagramAcc.txt", "r")
    for i in file:
        driver.get(i)
        element = driver.find_element(By.XPATH, '//*[@id="mount_0_0_Fu"]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
        element.click()
        element1 = driver.find_element(By.XPATH, '//*[@id="mount_0_0_pn"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
        element1.send_keys(word)
    

confirm = pyautogui.confirm('before we get started plz notes that this program is just test and any use of it in bad way you are the responsible about it ?' ,buttons=['yes','no'])
if confirm == "yes":
    try:
        Hashtags = pyautogui.prompt(text='ENTER THE searching_for_Hashtags ', title='SPAM ' , default='')
        opening_instagram()
        sleep(1)
        searching_for_hashtags(name)
        sleep(1)
        WebPageWait()
        sleep(1)
        word = pyautogui.prompt(text='ENTER MESSEGE', title='SPAM ' , default='HELLO')
        find_Acc_and_follow(word)
    except:
        sys.exit()
else:
    sys.exit()
