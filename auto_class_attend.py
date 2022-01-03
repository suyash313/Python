import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
dr = webdriver.Chrome('D:\\chrome driver\\chromedriver.exe', chrome_options=chrome_options)

chrome_options.add_experimental_option('prefs', {'profile.default_content_setting_values.media_stream_mic': 1})

dr.get('https://learn.upes.ac.in/webapps/login/')
wait = WebDriverWait(dr, 600)

dr.find_element_by_css_selector('.button-1').click()

username = dr.find_element_by_id("user_id")
username.click()
username.send_keys("5000*******")

password = dr.find_element_by_name("password")
password.click()
password.send_keys("enterpassword")

dr.find_element_by_id('entry-login').click()

time.sleep(15)
dr.find_element_by_id('main-content-inner').click()

html = dr.find_element_by_tag_name('html')
html.send_keys(Keys.PAGE_DOWN)
html.send_keys(Keys.PAGE_DOWN)
time.sleep(7)
dr.find_element_by_class_name('bb-close').click()
time.sleep(4)

dr.find_element_by_partial_link_text(
    'Software Engineering & Project Mgmt.2021.83.BT-CSE-Spz-BDATA-III-B1.BT-CSE-Spz-BDATA-III-B2.VR_B_1728').click()
time.sleep(7)
dr.find_element_by_css_selector('.ultra-collab .select-wrapper .join-session').click()
time.sleep(3)
dr.find_element_by_link_text('Course Room').click()
time.sleep(20)
el = dr.find_elements_by_xpath("//button[contains(string(), 'x')]")[0]
el.click()
# action = webdriver.common.action_chains.ActionChains(dr)
# action.move_to_element_with_offset(el, 5, 5)
# action.click()
# action.perform()

dr.find_element_by_css_selector('×').click()
time.sleep(3)

dr.find_element_by_class_name('close').click()
