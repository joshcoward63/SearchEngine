words = ['firstword', 'secondword', 'thirdword']
site = urllib.request.urlopen(link).read()
for word in words:
    if word in site:
       print(word)
    else:
       print(word, "not found")
