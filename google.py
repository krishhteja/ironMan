from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import wikipedia

def open(command):
    driver = webdriver.Firefox()
    print("Opening firefox")
    driver.get("https://www.google.com")
    inputElement = driver.find_element("name", 'q')
    inputElement.send_keys(command)
    inputElement.send_keys(Keys.ENTER)

def image(command):
    driver = webdriver.Firefox()
    print("Opening firefox")
    driver.get("https://www.images.google.com")
    inputElement = driver.find_element("name", 'q')
    inputElement.send_keys(command)
    inputElement.send_keys(Keys.ENTER)

def youtube(command):
    driver = webdriver.Firefox()
    print("Opening firefox")
    driver.get("https://www.youtube.com")
    inputElement = driver.find_element("name", "search_query")
    inputElement.send_keys(command)
    inputElement.send_keys(Keys.ENTER)

def whoIs(query, sessionID="general"):
    try:
        return wikipedia.summary(query)
    except:
        for newquery in wikipedia.search(query):
            try:
                return (wikipedia.summary(newquery))
            except:
                pass
    return ("I don't know about "+query)

if __name__ == '__main__':
    print("hello! Logs In google")