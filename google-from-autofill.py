from selenium import webdriver
import time
# data store radio button element
data = []
# textbox store textbox element
textbox = {}
link = input('link : ')
around = input("How many element in your from : ")
around = int(around)
for k in range(around):
    # you need to coppy xpath and put to element
    # input element respectively
    h = input("have textbox : yes , no => ")
    h2 = input("have button : yes , no => ")
    if(h=='yes'):
        element2 = input('xpath textbox : ')
        keys = input('your answer : ')
        textbox[element2] = keys
    elif(h2 == 'yes'):
        element = input('button , radio element : ')
        data.append(element)
loop = input('input your loop : ')
loop = int(loop)
for i in range(loop):
    web = webdriver.Chrome()
    web.get(link)
    time.sleep(2)
    for j in textbox:
            entry_btn = web.find_element('xpath',j)
            entry_btn.send_keys(textbox[j])
    for j in data:
            first_btn = web.find_element('xpath',j)
            first_btn.click()
