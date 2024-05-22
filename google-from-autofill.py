import os
import subprocess
import sys

# Define required packages
required_packages = ['selenium']

# Function to install missing packages
def install_dependencies():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", *required_packages])

# Check if dependencies are installed, if not, install them
try:
    from selenium import webdriver
except ImportError:
    print("Selenium package not found. Installing...")
    install_dependencies()
    from selenium import webdriver
    
import time
import random

# Data store radio button elements
radio_button_elements = []

# Textbox store textbox elements
textboxes = {}
link = input('Link: ')
shuffle_option = input("Do you want to shuffle (y/n)? : ")

if shuffle_option == 'y':
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
        elif textbox_option == "no":
            while True:
                    try:
                        element_container = int(input("How many container :"))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid integer.")
            shuffled_elements = [[] for _ in range(element_container)]
            for m in range(element_container):
                shuffled_elements[m] = []
                while True:
                    try:
                        container_size = int(input("How many items in container: "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid integer.")
                for n in range(container_size):
                    print("number" , n+1 , end=" | ")
                    element = input('Button or radio element : ')
                    shuffled_elements[m].append(element)
        else:
            continue
    while True:
        try:
            loop_count = input('Input number of loops: ')
            loop_count = int(loop_count)
            break
        except Exception as e:
            continue

    for i in range(loop_count):
        print("NUMBER : ", i + 1)
        web = webdriver.Chrome()
        web.get(link)
        time.sleep(2)
        selected_items = [random.choice(sublist) for sublist in shuffled_elements]

        for xpath, answer in textboxes.items():
            try:
                entry_textbox = web.find_element('xpath', xpath)
                entry_textbox.send_keys(answer)
            except Exception as e:
                continue

        for item_xpath in selected_items:
            try:
                element = web.find_element('xpath', item_xpath)
                element.click()
            except Exception as e:
                continue
        time.sleep(2)

else:
    while True:
        try:
            element_count = input("How many elements in your form: ")
            element_count = int(element_count)
            break
        except ValueError:
            continue
    for k in range(element_count):
        textbox_option = input("Do you have a textbox? (yes/no): ")
        if textbox_option == 'yes':
            textbox_xpath = input('Xpath of textbox: ')
            answer = input('Your answer: ')
            textboxes[textbox_xpath] = answer
        else :
            element_xpath = input('Button or radio element: ')
            radio_button_elements.append(element_xpath)
    while True:
        try:   
            loop_count = input('Input number of loops: ')
            loop_count = int(loop_count)
            break
        except Exception as e:
            continue

    for i in range(loop_count):
        print("NUMBER : ", i + 1)
        web = webdriver.Chrome()
        web.get(link)
        time.sleep(2)
        for xpath, answer in textboxes.items():
            try:
                entry_textbox = web.find_element('xpath', xpath)
                entry_textbox.send_keys(answer)
            except Exception as e:
                continue
        for xpath in radio_button_elements:
            try:
                element = web.find_element('xpath', xpath)
                element.click()
            except Exception as e:
                continue