from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from uuid import uuid4
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
import undetected_chromedriver as uc

#initial points = 74


while True:
    
    print("[+] Initializing Browser")
    
    #options = Options()
    #options.add_argument("start-maximized")

    # Chrome is controlled by automated test software
    #options.add_experimental_option("excludeSwitches", ["enable-automation"])
    #options.add_experimental_option('useAutomationExtension', False)
    driver = uc.Chrome(headless=True, use_subprocess=False)
    
    print("[+] Navigating to Referal Link")
    
    driver.get("https://wn.nr/kVs8UzY")
    
    print("[+] Scrolling to bottom")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    print("[+] Clicking Newsletter")
    newsletter = driver.find_element(By.CLASS_NAME, "email_subscribe-border")
    newsletter.click()
    
    print("[+] Clicking Agree")
    driver.find_element(By.CLASS_NAME, "opt-in-checkbox").click()
    
    print("[+] Finding Form")
    form = driver.find_element(By.CLASS_NAME, "entry_details")
    
    div = form.find_element(By.CLASS_NAME, "form-actions")
    
    print("[+] Clicking Continue")
    driver.implicitly_wait(10)
    btn = div.find_element(By.TAG_NAME, "button").click()
    
    driver.implicitly_wait(5)
    
    print("[+] Entering Name")
    name = driver.find_element(By.XPATH, "//div[@id='em7325932']//div[contains(@class,'expandable')]//div[contains(@class,'expanded-view ng-scope')]//form[contains(@name,'contestantForm')]//fieldset[@class='inputs ng-scope']//div[@class='form-horizontal']//div//input[@placeholder='Alice Smith']")

    name.click()
    name.send_keys(str(uuid4()))
    
    print("[+] Entering Email")
    email = driver.find_element(By.XPATH, "//div[@id='em7325932']//div[contains(@class,'expandable')]//div[contains(@class,'expanded-view ng-scope')]//form[contains(@name,'contestantForm')]//fieldset[@class='inputs ng-scope']//div[@class='form-horizontal']//div//input[@placeholder='alice.smith@example.com']")
    email.click()
    email.send_keys(f"{uuid4()}@gmail.com")
    
    print("[+] Agreeing")
    agree = driver.find_element(By.XPATH, "//form[contains(@class,'contestant compact-box form-compact ng-scope ng-invalid ng-invalid-required ng-valid-pattern ng-valid-email ng-dirty ng-valid-parse')]//div//div//span[contains(text(),'I am at least 18 years of age (required)')]")
    agree.click()
    
    print("[+] Saving")
    button = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/span[1]/button[1]/span[2]")
    button.click()
    
    sleep(3)
    driver.close()
    
    sleep(10)
    