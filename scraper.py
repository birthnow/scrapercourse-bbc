import requests
from bs4 import BeautifulSoup

for page in range(1,4):
    re = requests.get(f'https://www.bbc.com/zhongwen/trad/topics/c83plve5vmjt/page/{page}')
    soup = BeautifulSoup(re.text, 'html.parser')

    title = soup.find_all('span', {'class':'lx-stream-post__header-text gs-u-align-middle'})

    title_list = []
    for i in title:
        title_list.append(i.text)

    urls = soup.find_all('a', {'class':'qa-heading-link lx-stream-post__header-link'})
    url_title = 'https://www.bbc.com/'

    tag_list = []
    for i in urls:
        sub_respon = requests.get(url_title + i.get('href'))
        soup = BeautifulSoup(sub_respon.text, 'html.parser')
        sub_title = soup.find_all('li', {'class':'bbc-1msyfg1 e1hq59l0'})
        for i in sub_title:
            tag_list.append(i.text)

    print(f'第{page}頁')
    print(title_list)
    print(tag_list)