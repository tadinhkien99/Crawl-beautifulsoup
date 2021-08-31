from bs4 import BeautifulSoup
import requests
from lxml import etree
import os

link = "https://www.leuchtturm.de/"
# parse = bbs(response.text)
#
# option = parse.find("article", id="content")
# for op in option:
#     link_download = op.get('src')
#     print(link_download)
# #print(option)

# //*[@id="app"]/div/div[4]/div[1]/div/div/div[1]/figure[7]/div/div[1]/div/div/a/div/div[2]/div/img
# //*[@id="app"]/div/div[4]/div[1]/div/div/div[1]/figure[5]/div/div[1]/div/div/a/div/div[2]/div/img
# //*[@id="app"]/div/div[4]/div[1]/div/div/div[2]/figure[4]/div/div[1]/div/div/a/div/div[2]/div/img
def download_chapter(link):
    i = 0
    response = requests.get(link)
    soup = BeautifulSoup(response.content, "html.parser")
    # links = soup.find('ol', {'class':'discussionListItems'}).find_all('li')
    # for li in links:
    dom = etree.HTML(str(soup))
    categories_1 = dom.xpath("/html/body/div[2]/div/div[1]/div[3]/div[2]/div/div/div/div/a/@href")
    # print(b)
    for category_1 in categories_1:
        print(k)
    #     # print('https://kenhsinhvien.vn/'+ k)
    #     new_page = requests.get('https://kenhsinhvien.vn/'+ k)
    #     new_pages = BeautifulSoup(new_page.content)
    #     new_img = etree.HTML(str(new_pages))
    #     img = new_img.xpath("//div[@style='text-align: center']/img/@src")
    #     for ii in img:
    #         if "http" in ii:
    #             print(ii)
    #             with open(r'C:/Users/DELL/PycharmProjects/beautiful_soup/download/'+str(i) + '.jpg','wb') as f:
    #                 f.write(requests.get(ii).content)
    #                 i += 1

    # if not os.path.exists('download'):
    #     os.mkdir('download')
    # count=0
    # i=0
    # for li in links:
    #     link_download=li.get('src')
    #     print(link_download)
    #
    #     if "http" in link_download:
    #         with open(r'C:/Users/DELL/PycharmProjects/beautiful_soup/download/'+str(i) + '.jpg','wb') as f:
    #             f.write(requests.get(link_download).content)
    #             i += 1
download_chapter(link)
