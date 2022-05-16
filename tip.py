import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
}

try:
    re = requests.get('https://www.bbc.com/zhongwen/trad/topics/c83plve5vmjt', headers = headers, timeout = 5)

    if re.status_code == 200:
        soup = BeautifulSoup(re.text, 'html.parser')

        title = soup.find_all('span', {'class':'lx-stream-post__header-text gs-u-align-middle'})

        if title: 
            title_list = []
            for i in title:
                title_list.append(i.text)
            print(title_list)
        else:
            print('元素不存在!')

    else:
        print('status not 200')
except Exception as e:
    print(str(e))