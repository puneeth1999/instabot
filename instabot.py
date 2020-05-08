import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
import os
from password import pw
from password import us
import time

#Driver for chrome
driver = webdriver.Chrome()

#Page to retrieve
driver.get('https://www.instagram.com/')
sleep(2)

#Username
driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')\
    .send_keys(us)
#password
driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')\
    .send_keys(pw)
#login
driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]')\
    .click()
#NOT NOW button
sleep(4)
driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
#Click on the name <a> tag
sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a')\
    .click()

#Followers
sleep(5)
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')\
    .click()
sleep(3)

#The Scroll Box
sleep(3)
scroll_box = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
last_ht, ht = 0, 1
tok = time.time()
follower_count = 0
while last_ht != ht:

    sleep(1)
    # last_ht = ht
    ht = driver.execute_script('''
    arguments[1].scrollTo(arguments[0], arguments[1].scrollHeight);
    
    ''',last_ht, scroll_box)

    follower_count += 1
    tik  = time.time()

    if(tik - tok >= 40):
        break
#unordered_list
ul = scroll_box.find_element_by_tag_name('ul')

# #inside_div
# ins_div = ul.find_element_by_class_name('PZuss')

#links
links = ul.find_elements_by_tag_name('a')

names_followers = [name.text for name in links if name.text != '']



#Closing button X
driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click()

#List of following
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click()


#Scroll box
sleep(2)
scroll_box = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')

last_ht, ht = 0, 1
tok = time.time()
following_count = 0
while last_ht != ht:

    sleep(1)
    # last_ht = ht
    ht = driver.execute_script('''
    arguments[1].scrollTo(arguments[0], arguments[1].scrollHeight);

    ''', last_ht, scroll_box)

    following_count += 1
    tik = time.time()

    if (tik - tok >= 40):
        break



#Unordered List
ul_f = scroll_box.find_element_by_tag_name('ul')
#list items
links_f = ul_f.find_elements_by_tag_name('a')


names_following = [name.text for name in links_f if name.text != '']





'''______________PEOPLE GHOSTING YOU_____________'''
c = 0
print('\n\n')
for n in names_following:
    if n in names_followers:
        continue
    else:
        c += 1
        print(n,'is ghosting you' )
print('\n\n\n\n')
print(c,'number of people are ghosting you as of now')
print('\n\n\n\n')

'''_____________PEOPLE YOU'RE GHOSTING_________'''

k = 0
print('\n\n')
for n in names_followers:
    if n in names_following:
        continue
    else:
        k += 1
        print('You\'re ghosting', n)
print('\n\n\n\n')
print('You have been ghosting', k, 'number of people as of now')



driver.close()