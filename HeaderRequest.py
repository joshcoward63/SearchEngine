
# import all the required libraries
import requests
from bs4 import BeautifulSoup
  
# target url
url = 'https://www.somedomain.org/'
  
# requests instance
reqs = requests.get(url)
  
# used BeaitifulSoup module
soup = BeautifulSoup(reqs.text, 'html.parser')
  
# shows the title
print("Title of the website is : ")
for title in soup.find_all('title'):
    print(title.get_text())
