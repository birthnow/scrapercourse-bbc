import requests
from bs4 import BeautifulSoup


re = requests.get('https://www.bbc.com/zhongwen/trad/topics/c83plve5vmjt')

soup = BeautifulSoup(re.text, 'html.parser')

title = soup.find_all('span', {'class':'lx-stream-post__header-text gs-u-align-middle'})

title_list = []
for i in title:
    title_list.append(i.text)
print(title_list)
