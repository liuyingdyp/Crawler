'''
抓取豆瓣图书 Top250
字段：书名
      评分
      作者
库： 内置库 urllib
     第三方库 lxml
面向函数编程
'''
from urllib import request
import urllib
from lxml import etree
import time
# 文件IO对象
with open('douban.txt','a',encoding='utf-8') as fp:
    # 获取源码方法
    def MakePage():
        i = 0
        while i <= 225:
            base_url = "https://book.douban.com/top250?start={0}".format(i)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
            req = urllib.request.Request(url=base_url, headers=headers)
            re = urllib.request.urlopen(req).read()
            print(re)
            time.sleep(2)
            i += 25
            html = re.decode('utf-8') # 获取源码并解码
            htmls = etree.HTML(html)  # 处理源码
            StoInfo(htmls)  # 调清洗数据方法并传值

    # 清洗数据并保存
    def StoInfo(htmls):
        book_name = htmls.xpath('//div[@class="pl2"]/a/@title') # 书名
        ratings = htmls.xpath('//span[@class="rating_nums"]/text()') # 评分
        writers = htmls.xpath('//p[@class="pl"]/text()') # 作者
        lens = len(book_name)  #获取一个字段的长度
        i = 0
        while i < lens:
            print('loading......')
            book_names = book_name[i] # 遍历书名
            rating = ratings[i]       # 遍历评分
            writer = writers[i].split('/')[0]       # 遍历作者
            fp.write('《'+book_names+'》' + '  评分:'+rating+'  作者：'+writer + '\n' )
            i += 1

    if __name__ == '__main__':
        MakePage()



