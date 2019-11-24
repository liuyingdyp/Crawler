import requests
import re
import os
import urllib.request
import time
# 下载视频
def download():
    k = 1
    while k <= 2:
        # 获取网页源代码
        url = "http://www.budejie.com/video/{0}".format(k)
        # 模拟浏览器去请求服务器
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        # 状态码
        html = requests.get(url, headers=headers)
        # 获取视频id   .*？匹配所有
        reg = 'data-mp4="(.*?)"'
        video_url = re.findall(reg, html.text)
        name = '<div class="j-video-c" data-title="(.*?)"</div>'
        video_name = re.findall(name, html.text)
        k += 1
        print(video_url)
        print(video_name)
        for i in video_url:
            print('正在下载视频%s' % i)
            path = 'video'
            if not os.path.exists(path):
                os.makedirs(path)
            file_path = path + '/%s' % i.split('/')[6] + ".mp4"
            urllib.request.urlretrieve(i, file_path)
download()