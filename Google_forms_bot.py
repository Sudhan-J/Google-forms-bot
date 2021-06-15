from selenium import webdriver
import pyautogui
import time
browser = webdriver.Chrome('C:/Users/sudhan/Documents/git_rep_projects/PYTHON/Google-foms-bot/chromedriver.exe')
browser.get("https://forms.gle/EzMJpE31bndwei79A")
browser.maximize_window()
time.sleep(1)
#email filling
mail = "abc@gmail.com"
email = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
email.send_keys(mail)
#name filling
name = "user_name"
user_name = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
user_name.send_keys(name)
#USN or register number filling
usn = "4JN19CS107"
user_usn = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
user_usn.send_keys(usn)
#drop down menu selection
dropmenu = browser.find_element_by_class_name('quantumWizMenuPaperselectOption')
dropmenu.click()
time.sleep(1)
dropdown1 = browser.find_element_by_css_selector('.exportSelectPopup [data-value="4B"]')
dropdown1.click()
time.sleep(1)
#automating mouse scroll using selenium
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#phone number filling
number = "1234567891"
phone_number = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
phone_number.send_keys(number)
#to select date I am using pyautogui module
cords = pyautogui.locateCenterOnScreen('dateicon.png')
pyautogui.click(cords)
cords1 = pyautogui.locateCenterOnScreen('today.png')
pyautogui.click(cords1)
#automating mouse click on submit button
time.sleep(1)
submit_button = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
submit_button.click()
time.sleep(1)
#closing the browser
browser.quit()

