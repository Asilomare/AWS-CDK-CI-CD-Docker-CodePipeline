import requests
from bs4 import BeautifulSoup

URL = "https://www.worldometers.info/coronavirus/"
page = requests.get(URL)


soup = BeautifulSoup(page.content, "html.parser")


results = soup.findAll("div", class_='maincounter-number')

data_dict = {"Cases":0, "Deaths":0, "Recovered":0}
c = 0
for span in results:
    data_dict[c]=span.text
    c = c+1
    
    
data_list = []
for span in results:
    data_list.append(span.text)
    print(span.text)
    


