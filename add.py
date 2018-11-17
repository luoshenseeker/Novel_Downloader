import requests
from lxml import etree

url = "https://m.23us.so"

#open a file
novel = open("C:/users/63559/desktop/novel.txt", mode = "a", encoding = "utf-8")
for i in range(53, 68):
    url_add = "/wapbook/1240/{}.html".format(i)
    catalogue_req = requests.get(url + url_add)
    catalogue_req.encoding = "utf-8"
    catalogue_html = etree.HTML(catalogue_req.text)

    chapter_page = catalogue_html.xpath("//*[@class = 'chapter']")
    chapter_list = chapter_page[1].xpath(".//@href")
    for chapter in chapter_list:
        article_req = requests.get(url + chapter)
        article_req.encoding = "utf-8"
        article_html = etree.HTML(article_req.text)
        
        #Get title
        title = article_html.xpath("//h1")[0].text
        novel.write(title + "\n\n\n")
        print(title)

        #Get content
        article = article_html.xpath("//*[@id='nr1']")[0]
        #first paragraph
        first = article.text.strip()
        novel.write("    " + first + "\n")

        #next paragraphs
        paras = article.xpath("//br")
        for para in paras:
            tail = para.tail
            if tail is not None:
                follow = tail.strip()
                novel.write("    " + follow + "\n")
        novel.write("\n"*3 + "#"*30 + "\n")
    
print("success")