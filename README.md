# Automated Form Submission using Selenium

This Python script utilizes the Selenium library to automate the process of filling out a web form. The script prompts the user for relevant information such as the target website link, the number of elements in the form, and details about each form element (text boxes, buttons, and radio elements). It then performs the specified actions in a loop.

## Prerequisites

Before running the script, ensure you have the following installed:

-   **Python**: [Download Python](https://www.python.org/downloads/)
-   **Selenium**: You can install Selenium via pip: `pip install selenium`
-   **ChromeDriver**: Download the appropriate version from [ChromeDriver website](https://sites.google.com/chromium.org/driver/) and ensure it's in your system's PATH.

## How to Use

1.  Run the script.
2.  Enter the target website link when prompted.
3.  Specify whether you want to shuffle elements or not. If shuffling, provide details about elements in each container.
4.  For each form element, specify whether it is a textbox or a button/radio element and provide the XPath.
5.  If the element is a textbox, enter the desired input.
6.  If the element is a button or radio element, simply provide the XPath.
7.  Enter the number of times you want to submit the form (loop count).

## Example

Here's an example of how to use the script:

1. Enter the target website link: `https://example.com/form`
2. Specify whether to shuffle elements (y/n): `y`
3. Provide details about elements in containers.
4. Input number of loops: `5`
5. The script will then fill out the form 5 times with shuffled elements.

## Notes

- Ensure that the ChromeDriver version is compatible with your Chrome browser version.
- Make sure to provide accurate XPaths for form elements to ensure proper automation.
- It's recommended to test the script on a test website before using it on a production site.


https://youtu.be/t0DmwNrfVqo?si=dYJrGixShTA-UJ9R
