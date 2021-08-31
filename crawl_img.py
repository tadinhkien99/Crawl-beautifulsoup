from bs4 import BeautifulSoup
import requests
from lxml import etree
import os

link = "https://www.istockphoto.com/vi/search/2/image?mediatype=photography&page=1&phrase=house"
# parse = bbs(response.text)
#
# option = parse.find("article", id="content")
# for op in option:
#     link_download = op.get('src')
#     print(link_download)
# #print(option)

# /html/body/div[2]/section/div/main/div/div/div/div[2]/div/div[3]/div[1]/article/a/figure/img
# /html/body/div[2]/section/div/main/div/div/div/div[2]/div/div[3]/div[2]/article/a/figure/img
# /html/body/div[2]/section/div/main/div/div/div/div[2]/div/div[3]/div[3]/article/a/figure/img
def download_chapter(link):
    count=3000
    for page in range(45,70):
        link = "https://www.istockphoto.com/vi/search/2/image?mediatype=photography&page=" + str(page) + "&phrase=house"
        print(link)
        i = 1
        response = requests.get(link).text
        soup = BeautifulSoup(response, 'html.parser')
        # links = soup.find('ol', {'class':'discussionListItems'}).find_all('li')
        # for li in links:
        dom = etree.HTML(str(soup))
        while True:
            src = dom.xpath("/html/body/div[2]/section/div/main/div/div/div/div[2]/div/div[3]/div["+ str(i) +"]/article/a/figure/img/@src")

            i+=1
            if src==[]:
                break
            else:

                # print(requests.get(src[0]).content)
                with open(r'C:\Users\DELL\Downloads\img_crawl/'+str(count) + '.jpg','wb') as f:
                    f.write(requests.get(src[0]).content)
                print(count)
                count += 1


    # for k in b:
    #     # print('https://kenhsinhvien.vn/'+ k)
    #     new_page = requests.get('https://kenhsinhvien.vn/'+ k)
    #     new_pages = BeautifulSoup(new_page.content)
    #     new_img = etree.HTML(str(new_pages))
    #     img = new_img.xpath("//div[@style='text-align: center']/img/@src")
    #     for ii in img:
    #         if "http" in ii:
    #             print(ii)

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
