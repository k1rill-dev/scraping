from datetime import datetime
import requests
from bs4 import BeautifulSoup
import json

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50"
}


def get_ongoing():
    url = 'https://jut.su'
    req = requests.get(url=url, headers=headers)
    response = req.text
    soup = BeautifulSoup(response, 'lxml')

    titles = soup.find('div', class_='media_b clear new_all_other_last_eps').find_all('div', class_='media_content')

    titles_data = []
    for item in titles:
        title_head = item.find('div', class_='b-g-title').text.strip()
        title_href = item.find('a', class_='media_link l_e_m_l').get('href')
        dictt = {
            'head' : title_head,
            'link' : title_href
        }
        titles_data.append(dictt)
    print(titles_data)
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(titles_data, file, indent=4, ensure_ascii=False)

def main():
    get_ongoing()

if __name__ == '__main__':
    main()
