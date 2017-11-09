import time
from sys import stdout
from datetime import datetime
from getpass import getpass
from pushbullet import Pushbullet
from selenium import webdriver


def print_noendl(text):
    stdout.write(text)
    stdout.flush()


pb_key = input('PB API Key: ')
pb = Pushbullet(pb_key)

print('- UCSD Credentials -')
username = input('Username: ')
password = getpass()

driver = webdriver.Chrome()
driver.get('https://act.ucsd.edu/webreg2/start')

e = driver.find_element_by_id('ssousername')
print(driver.title)
e.send_keys(username)
e = driver.find_element_by_id('ssopassword')
e.send_keys(password)
e = driver.find_element_by_class_name('sso-button')
e.click()

e = driver.find_element_by_id('startpage-button-go')
print(driver.title)
e.click()

while True:
    e = driver.find_element_by_id('grid-edit-plan-id-wait-6')
    if not e.get_attribute('disabled'):
        print('ENROLL, NOW!!!')
        pb.push_note('course_snipe.py', 'ENROLL, NOW!!!')
        break
    print_noendl('(%s) Refreshing' % datetime.now())
    for _ in range(5):
        print_noendl('.')
        time.sleep(1)
    print()
    driver.refresh()
