# importing modules
from bs4 import BeautifulSoup
import urllib.request

# providing url
url = "https://www.geeksforgeeks.org/how-to-automate-an-excel-sheet-in-python/?ref=feed"

# opening the url for reading
html = urllib.request.urlopen(url)

# parsing the html file
htmlParse = BeautifulSoup(html,'html.parser')

# getting all the paragraphs
for para in htmlParse.find_all("p"):
    print(para.get_text())
# getting  all data between open body tag and closed body tag
'''for paras in htmlParse.find_all("body"):
    print(paras.get_text())
'''