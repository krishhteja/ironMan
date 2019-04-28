from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import googleapiclient

def open(command):
    driver = webdriver.Firefox()
    print("Opening firefox")
    driver.get("https://www.google.com")
    inputElement = driver.find_element_by_name('q')
    inputElement.send_keys(command)
    inputElement.send_keys(Keys.ENTER)

if __name__ == '__main__':
    print("hello! Logs In google")