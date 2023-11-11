from selenium import webdriver
import time
data = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span']
textbox = {}
# # link = input('link : ')
# around = input("How many rounds : ")
# around = int(around)
# for k in range(around):
#     # you need to coppy xpath and put to element
#     h = input("have textbox : yes , no => ")
#     h2 = input("have button : yes , no => ")
#     if(h=='yes'):
#         element2 = input('xpath textbox : ')
#         keys = input('your answer : ')
#         textbox[element2] = keys
#     elif(h2 == 'yes'):
#         element = input('button , radio element : ')
#         data.append(element)
loop = input('input your loop : ')
loop = int(loop)
for i in range(loop):
    web = webdriver.Chrome()
    web.get("https://forms.gle/PxHxoVDDsgvmftg98")
    time.sleep(2)
    # data = ['//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span']
    for j in textbox:
            entry_btn = web.find_element('xpath',j)
            entry_btn.send_keys(textbox[j])
    for j in data:
            first_btn = web.find_element('xpath',j)
            first_btn.click()
