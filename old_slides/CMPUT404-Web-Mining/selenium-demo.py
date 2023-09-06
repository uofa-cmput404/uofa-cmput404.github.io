# selenium example
# (c) 2019 Abram Hindle, Selenium Project
# Under the same license as python selenium module
# License: Apache Software License (Apache 2.0)

# pip3 install --user selenium

# you need chromedriver http://chromedriver.chromium.org/downloads
# e.g. https://chromedriver.storage.googleapis.com/74.0.3729.6/chromedriver_linux64.zip
import os, sys
# Danger Danger Will Wobinson
curdir = "."
os.environ['PATH'] = f"{curdir}:{os.environ.get('PATH')}"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
# driver = webdriver.Chrome('./chromedriver',chrome_options=chrome_options)
driver = webdriver.Chrome(chrome_options=chrome_options)
print("Driver ready")
driver.get("https://news.google.ca/")
driver.get("https://search.twitter.com")

inputclass = 'Ax4B8'
search = driver.find_element_by_css_selector(f"input")
topic = "programmer humor"
sleep(1)
search.send_keys(topic)
search.send_keys("\n")
sleep(1)
#linkclass = "VDXfz"
#searches = driver.find_elements_by_css_selector(f"article a.{linkclass}")
driver.find_elements_by_partial_link_text('Webservices')[0].click()
sleep(1)

# driver.find_element_by_tag_name - find element by tagname

# find_element_by_partial_link_text

# find_elements_by_css_selector

driver.close()
