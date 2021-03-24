from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from lxml import html
import requests

import requests
page = requests.get("https://www.boisestate.edu/coen-cs/")
contents = page.content

# page = requests.get('http://example.com/ex/somewebpage.html')
# tree = html.fromstring(page.content)

from bs4 import BeautifulSoup
soup = BeautifulSoup(contents, 'html.parser')
soup.find_all('a')


"""Function is used to get body tag information"""
def get_body_tags(page):
    soup = BeautifulSoup(page, "html.parser")
    body_text = soup.find("body").text
    return body_text

# print(get_body_tags(contents))