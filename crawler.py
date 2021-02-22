from bs4 import BeautifulSoup
import requests
import re

source_code = requests.get("https://www.boisestate.edu/coen-cs/")
soup = BeautifulSoup(source_code.content, 'html.parser')

links = []

"""
url - the starting point at which the web crawler begins crawling
Returns a list of urls from that page
"""
def get_first(url):
    links = []
    source_code = requests.get(url)
    soup = BeautifulSoup(source_code.content, 'html.parser')
    for link in soup.find_all('a'):
        if link.get("href") != None and "http" in link.get("href"):
            links.append((link.get('href')))
    return links

def get_all_urls( links):
    links2 = []  
    for link in links:
        source_code = requests.get(link)
        soup = BeautifulSoup(source_code.content, 'html.parser')
        for link_on_page in soup.find_all('a'):
            if link_on_page.get("href") != None and link_on_page.get('href') not in links and "http" in link_on_page.get("href") and len(link_on_page.get("href")) < 100:
                links2.append(link_on_page.get("href"))
    links = links + links2
    return links
    # else:          
    #     linksJoined = []
    #     for i in range(times):
    #         for link in links:
    #             source_code = requests.get(link)
    #             soup = BeautifulSoup(source_code.content, 'html.parser')
    #             for link_on_page in soup.find_all('a'):
    #                 if link_on_page.get("href") != None and link_on_page.get('href') not in links and "http" in link_on_page.get("href"):
    #                     links2.append(link_on_page.get("href"))

    #     linksJoined = linksJoined + links + links2
    #     links = links2
    #     links2 = []
    # return linksJoined

first_set = get_first("https://www.boisestate.edu/coen-cs/")

urls = get_all_urls(first_set)
print(len(first_set))
print(len(urls))
for i in range(2):
    urls = get_all_urls(urls)
# [print(url) for url in urls]
print(len(urls))