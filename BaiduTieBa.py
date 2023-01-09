from urllib import request
import re
import time
import random

class BaiduTieBa:
    def __init__(self, baseURL, seeLZ):
        self.baseURL = baseURL
        self.seeLZ   = '?see_lz=' + str(seeLZ)

    # 根据url获取网页
    def fetchPage(self, pageNum=1):
        try:
            url      = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            requests = request.Request(url, headers=headers)
            response = request.urlopen(requests)
            html     = response.read().decode('utf-8')
            return html
        except:
            print('连接失败')
            return None

    # 获取帖子的标题
    def fetchTitle(self):
        page    = self.fetchPage()
        pattern = re.compile(r'(?<=<title>).*(?=_百度贴吧)')
        result  = re.search(pattern, page)
        if result:
            return result.group()
        else:
            return f'获取标题失败'

    # 获取帖子的总页数
    def fetchTotalPage(self):
        page    = self.fetchPage()
        pattern = re.compile(r'(?<=<span class="red">)\d*(?=</span>)')
        result  = re.search(pattern, page)
        if result:
            totalPage = int(result.group()) // 2
            return totalPage
        else:
            return f'获取页数失败'


if __name__ == '__main__':
    originURL = 'https://tieba.baidu.com/p/8179625573?frwh=index'
    headers   = {'User-Agent'     : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                    'Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
                 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
                 'Accept'         : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;'
                                    'q=0.8,application/signed-exchange;v=b3;q=0.9',
                 'Cookie'         : 'BAIDUID=95312DF85A14760C5DA6F73C54207CCC:FG=1;'
                                    'BIDUPSID=95312DF85A14760C5DA6F73C54207CCC; '
                 }
    post01    = BaiduTieBa(originURL, 0)
    method    = [post01.fetchTitle, post01.fetchTotalPage]
    
    for i in method:
        print(i())
        time.sleep(random.randrange(1,3) * 0.1)
