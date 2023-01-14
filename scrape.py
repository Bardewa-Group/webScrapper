# modules used = requests, bs4, html5lib
import requests
from bs4 import BeautifulSoup

url = "https://codewithharry.com"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

sajan = soup.findAll('p')

for i in sajan:
    print(i)
    print(' ')


print(soup.find(id='qna'))

exit()



title = soup.find('title').get_text()

links = soup.findAll('a')
container = set()
for i in links:
    container.add(i)

print(len(container))

for i in container:
    print(i)
    print(' ')