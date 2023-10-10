import urllib.request
from bs4 import BeautifulSoup

page = urllib.request.urlopen("https://www.sidefx.com/docs/houdini/ref/env.html").read()
soup = BeautifulSoup(page, 'html.parser')
a = soup.find_all('li', class_="env_variables_item item")
soup2 = BeautifulSoup(str(a), 'html.parser')
b = soup2.find_all('p', class_='label')
soup3 = BeautifulSoup(str(b), 'html.parser')
c = soup3.find_all('code')
s = [i.get_text() for i in c]
print(s)
with open('env_variables.txt', 'w') as f:
    for i in s:
        if i.isupper() and '"' not in i and '$' not in i:
            i = ' '.join(i.split())
            f.write(str(i) + '\n')
    f.write('PATH\n')
