from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

# Data store radio button elements
radio_button_elements = []

# Textbox store textbox elements
textboxes = {}
link = input('Link: ')
shuffle_option = input("Do you want to shuffle (y/n)? : ")

if shuffle_option == 'y':
    element_container = int(input("How many container :"))
    shuffled_elements = [[] for _ in range(element_container)]
    print("PLEASE ADD ALL ELEMENTS")
    print("IF FINISH PLEASE INPUT (end)")
    while True:
        textbox_option = input("Do you have a textbox? (yes/no/end): ")
        if textbox_option == 'end':
            break
        if textbox_option == 'yes':
            element_xpath = input('Xpath of textbox: ')
            answer = input('Your answer: ')
            textboxes[element_xpath] = answer
        else:
            for m in range(element_container):
                shuffled_elements[m] = []
                container_size = int(input("How many items in container: "))
                for n in range(container_size):
                    element = input('Button or radio element: ')
                    shuffled_elements[m].append(element)

    loop_count = input('Input number of loops: ')
    loop_count = int(loop_count)

    web = webdriver.Chrome()
    web.get(link)
    wait = WebDriverWait(web, 10)

    for i in range(loop_count):
        for xpath, answer in textboxes.items():
            entry_textbox = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            entry_textbox.send_keys(answer)

        selected_items = [random.choice(sublist) for sublist in shuffled_elements]
        for item_xpath in selected_items:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, item_xpath)))
            element.click()

else:
    element_count = input("How many elements in your form: ")
    element_count = int(element_count)
    for k in range(element_count):
        textbox_option = input("Do you have a textbox? (yes/no): ")
        button_option = input("Do you have a button? (yes/no): ")
        if textbox_option == 'yes':
            textbox_xpath = input('Xpath of textbox: ')
            answer = input('Your answer: ')
            textboxes[textbox_xpath] = answer
        else:
            element_xpath = input('Button or radio element: ')
            radio_button_elements.append(element_xpath)
    loop_count = input('Input number of loops: ')
    loop_count = int(loop_count)

    web = webdriver.Chrome()
    web.get(link)
    wait = WebDriverWait(web, 10)

    for i in range(loop_count):
        for xpath, answer in textboxes.items():
            entry_textbox = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            entry_textbox.send_keys(answer)

        for xpath in radio_button_elements:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element.click()

# Close the browser session after completion
web.quit()
