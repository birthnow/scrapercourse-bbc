import grequests
from bs4 import BeautifulSoup
import time


start_time = time.time()

links = [f'https://www.bbc.com/zhongwen/trad/topics/c83plve5vmjt/page/{page}' for page in range(1,4)]

reqs = (grequests.get(link) for link in links)
resps = grequests.imap(reqs, grequests.Pool(3))

for index, resp in enumerate(resps):
    soup = BeautifulSoup(resp.text, 'html.parser')

    title = soup.find_all('span', {'class':'lx-stream-post__header-text gs-u-align-middle'})

    title_list = []
    for i in title:
        title_list.append(i.text)

    urls = soup.find_all('a', {'class':'qa-heading-link lx-stream-post__header-link'})
    sub_links = ['https://www.bbc.com/' + url.get('href') for url in urls]
    sub_reqs = (grequests.get(sub_link) for sub_link in sub_links)
    sub_resps = grequests.imap(sub_reqs, grequests.Pool(10))
    

    tag_list = []
    for sub_resp in sub_resps:
        soup = BeautifulSoup(sub_resp.text, 'html.parser')
        sub_title = soup.find_all('li', {'class':'bbc-1msyfg1 e1hq59l0'})
        for i in sub_title:
            tag_list.append(i.text)

    print(f'第{index+1}頁')
    print(title_list)
    print(tag_list)

end_time = time.time()
print(f'總共花費{end_time-start_time}秒')