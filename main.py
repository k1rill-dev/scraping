import requests
from bs4 import BeautifulSoup
import json
import os
from dotenv import load_dotenv

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50"
}


def get_ongoing():
    url = "https://yummyanime.org"
    req = requests.get(url=url, headers=headers)
    response = req.text
    soup = BeautifulSoup(response, 'lxml')

    date = soup.find('div', class_='ksupdate_block').find('div', class_='ksupdate_block_date').text

    titles = soup.find('div', class_='ksupdate_block').find('ul', class_='ksupdate_block_list').find_all('li', class_='ksupdate_block_list_item')
    # for i in titles:
    #     print(i.text.strip())
    hrefs = soup.find('div', class_='ksupdate_block').find('ul', class_='ksupdate_block_list').find_all('a')
    # for i in hrefs:
    #     print("https://yummyanime.org" + i.get('href'))

    titles_data = []
    dictt = {}
    dict_sorted = {}
    for item in titles:
        title_head = item.find('div', class_='cell cell-1').text.strip()
        for i in hrefs:
            #print("https://yummyanime.org" + i.get('href'))
            title_href = "https://yummyanime.org" + i.get('href')
            # print(title_href)
            # print(title_head)
            dictt = {
                'head' : title_head,
                'link' : title_href
            }
            v_by_k = dict()
            for k, v in dictt.items():
                if v not in v_by_k:
                    v_by_k[v] = k

            dict_sorted = {v: k for k, v in v_by_k.items()}
            titles_data.append(dict_sorted)
    print(titles_data)
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(titles_data, file, indent=4, ensure_ascii=False)

def main():
    get_ongoing()

if __name__ == '__main__':
    main()
