"""Libraries"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from lxml import html
import requests
import re
import requests
# page = requests.get("https://www.boisestate.edu/coen-cs/people/faculty/")
# contents = page.content

# page = requests.get('http://example.com/ex/somewebpage.html')
# tree = html.fromstring(page.content)

from bs4 import BeautifulSoup
# soup = BeautifulSoup(contents, 'html.parser')
# soup.find_all('a')

"""Function is used to get title tag information"""
def get_title_tags(page):
    contents = page.content
    soup = BeautifulSoup(contents, "html.parser")
    try:
        title_text = soup.find("title").text
    except:
        title_text = ""
    return title_text

"""Function is used to get body tag information"""
def get_body_tags(page):
    contents = page.content

    soup = BeautifulSoup(contents, "html.parser")
    try:
        body_text = soup.find("body").text
    except:
        body_text = ""
    return body_text

"""Function is used to get information stored in an unordered list from webpage"""
def get_ul_tags(page):
    contents = page.content
    soup = BeautifulSoup(contents, "html.parser")
    ul = soup.find_all("ul")
    unordered_list = []
    for wrapper in ul:
        unordered_list.append(' '.join(wrapper.text.replace('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n',"@@@@@@").replace('\n',' ').replace('\t',"").split()).split("@@@@@@"))
    return unordered_list

# print(get_title_tags(contents))
