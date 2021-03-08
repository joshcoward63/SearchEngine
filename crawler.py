from bs4 import BeautifulSoup
import requests

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

"""
Arguments:
links - list of links/urls

Returns - list of all links grabbed from the inputted list of links including orignal lists
"""
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

#Inital list of urls grabbed from seed

# first_set = get_first("https://www.boisestate.edu/coen-cs/")

#List of all urls grabbed from all the links in the first_set including the original links

# urls = get_all_urls(first_set)
# print(len(first_set))
# print(len(urls))

#The following creates a list of links where depth is equal to the number of times we will grab links from the given
#For example a depth of 1 takes the original list of urls and grabs all the urls on each one of those links and adds them to a list
#A depth of 2 would then take the list or urls outputted by the depth 1 iteration and grab all the urls from all of those links 

# depth = 1
# for i in range(depth):
#     urls = get_all_urls(urls)

# print(len(urls))