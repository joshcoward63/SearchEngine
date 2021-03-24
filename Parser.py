from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from lxml import html
import requests

import requests
page = requests.get('http://examplesite.com')
contents = page.content

page = requests.get('http://example.com/ex/somewebpage.html')
tree = html.fromstring(page.content)

from bs4 import BeautifulSoup
soup = BeautifulSoup(contents, 'html.parser')
soup.find_all('a')

