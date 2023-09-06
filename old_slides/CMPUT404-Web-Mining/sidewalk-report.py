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

# go to https://permits.edmonton.ca/Default.aspx?PossePresentation=NewPermitSnow&PosseObjectDef=j_BYLAWCOMPLAINT&PosseMenuName=Complaints
# then inspect each element of the form
# writedown the ids of the elements

data = {
	"ComplainantFirstName_1188393_N0":"FirstName",
	"ComplainantLastName_1188393_N0":"Lastname",
	"ComplainantHouseNumber_1188393_N0":"777",
	"ComplainantStreet_1188393_N0":"777 AVENUE NW",
	"ComplainantPostalCode_1188393_N0":"T6G7G7",
	"ContactPhoneNumber_1188393_N0_1":"780",
	"ContactPhoneNumber_1188393_N0_2":"777",
	"ContactPhoneNumber_1188393_N0_3":"7777",
	"EmailAddress_1188393_N0":"youremail@gmail",
	"WebHouseNumber_1188393_N0":"Complaint House Number",
	"WebLookupStreet_1188393_N0":"Complaint Street NW",
	"WebSuite_1188393_N0":"Complaint Suite Number",
	"WBylawComments_1188390_N0":"Lots of ice on sidewalk. Neighbors have no ice. No maintenance in past week"
}

def fill_in_element(driver,elm,data):
    ''' find an element on the page and fill it in '''
    elem = driver.find_element_by_name(elm)
    elem.clear()
    elem.send_keys(data)
    elem.send_keys(Keys.RETURN)

def report_sidewalk(data):
    ''' go to the edmonton complaints page and fill it out '''
    driver = webdriver.Chrome()
    # driver.get("http://www.python.org")
    # go to this page
    driver.get("https://permits.edmonton.ca/Default.aspx?PossePresentation=NewPermitSnow&PosseObjectDef=j_BYLAWCOMPLAINT&PosseMenuName=Complaints")
    # make sure it is the right page
    assert "Web Application" in driver.title
   
    # for each key find the form element and complain 
    for key in data.keys():
        fill_in_element(driver,key, data[key])
    
    sleep(5)
    # remove this comment to actually submit the form
    return None
    driver.find_element_by_id('ctl00_cphBottomFunctionBand_ctl03_Submit').click()
    
    elms = driver.find_elements_by_css_selector('span[Id^=External]')
    #for elm in elms:
    #    print(elm.text)
    code = elms[0].text
    sleep(5)
    driver.close()
    return code

ctext = "weeks of no maintenance, lots of ice and snow, impassable for wheelchairs and strollers."
cols = ["WebHouseNumber_1188393_N0","WebLookupStreet_1188393_N0","WebSuite_1188393_N0","WBylawComments_1188390_N0"]

# list all the offenders (they tend to repeat)
complaints = [
	("11000","UNIVERSITY AVENUE NW","","west side corner lot %s" % ctext),
	("11000","UNIVERSITY AVENUE NW","","west side corner lot %s" % ctext),
	("11000","UNIVERSITY AVENUE NW","","west side corner lot %s" % ctext)
]

# complain on them!
for complaint in complaints:
    for i in range(0,len(cols)):
        k = cols[i]
        v = complaint[i]
        data[k] = v
    print(report_sidewalk(data))

