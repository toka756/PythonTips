import requests
from bs4 import BeautifulSoup

# yahoo japanのニュースを取ってくる

def download_page(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    r = requests.get(url, headers=headers)
    return r.text

def get_content(html, category):
    output = """ カテゴリ： {} タイトル：{} リンク：{} 日時：{}\n------------\n""" # 最终输出格式
    soup = BeautifulSoup(html, 'html.parser')
    con = soup.find('ul', class_='newsFeed_list')
    con_list = con.find_all('li', class_="newsFeed_item")
    for i in con_list:
        print("list i %s" % i)
        a = i.find('a', class_='newsFeed_item_link')
        text = a.find('div', class_='newsFeed_item_text')
        title = text.find('div', class_='newsFeed_item_title').string
        print('Fetch title %s' % title)
        link = a.get("href")
        date = text.find('div', class_='newsFeed_item_sub').find('div', class_='newsFeed_item_sourceWrap').find('time', class_='newsFeed_item_date').string
        save_txt(output.format(category, title, link, date))

def save_txt(*args):
    for i in args:
        with open('yahoo.txt', 'a') as f:
            print(i)
            f.write(i)


def main():
    category = ['domestic', 'world', 'business']
    for ca in category:
        url = 'https://news.yahoo.co.jp/topics/'+ca
        print('Start download url %s' % url)
        html = download_page(url)
        # print(html)
        get_content(html, ca)

if __name__ == "__main__":
    main()

main()







    
