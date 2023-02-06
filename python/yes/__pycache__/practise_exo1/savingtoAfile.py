import requests
from bs4 import BeautifulSoup

url="http://www.nytimes.com"
r=requests.get(url)
r_html=r.text
soup=BeautifulSoup(r_html,'lxml')
i=1
for link in soup.find_all('h3') :
     if link.get_text() != "Advertisement":    
        with open('webpagetitiles.txt', 'w') as open_file:
         open_file.write(link.get_text())   
        
        i=i+1   
