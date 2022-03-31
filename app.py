import time
import urllib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from contacts import Contact
from message import Message

contacts = Contact
message = Message

browser = webdriver.Chrome()
browser.get('https://web.whatsapp.com/')

while len(browser.find_elements_by_id("side")) < 1:
    time.sleep(1)

contact_list = contacts.read('data.json')
contact_list_clone = contact_list
for index, contact in enumerate(contact_list):
    if contact_list_clone[index]['sent'] == False:
        text = urllib.parse.quote(message.text())
        number = contact['number']
        link = f'https://web.whatsapp.com/send?phone={number}&text={text}'
        browser.get(link)
        while len(browser.find_elements_by_id("side")) < 1:
            time.sleep(1)
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
        time.sleep(3)
        contact_list_clone[index]['sent'] = True
        contacts.write('data.json', contact_list_clone)