from headers import headers
from urllib import request
import random
import time
import re


class Tools:
    # 替换BR标签为\n
    replaceBR         = re.compile('<br><br>|<br>')
    # 保留图片
    replaceImgPrefix  = re.compile('<img class="BDE_Image".*?src="')
    replaceImgSuffix  = re.compile('" size=.*?>')
    # 删除分隔符
    removeDIV         = re.compile('<div>|</div>')
    # 删除贴吧表情
    removeEmoji       = re.compile('<img class="BDE_Smiley".*?src=".*?" >')
    # 删除装扮框
    removeChatBox    = re.compile('<div class=.*?>')

    def replace(self, item):
        item = re.sub(self.replaceBR       , '\n', item)
        item = re.sub(self.replaceImgPrefix, ' ' , item)
        item = re.sub(self.replaceImgSuffix, ''  , item)
        item = re.sub(self.removeDIV       , ''  , item)
        item = re.sub(self.removeEmoji     , ''  , item)
        item = re.sub(self.removeChatBox   , ''  , item)
        if item == '':
            return 'emoji'
        return item


class BaiduTieBa:
    def __init__(self, baseURL, seeLZ):
        self.baseURL = baseURL
        self.seeLZ   = '?see_lz=' + str(seeLZ)

    # 根据url获取网页
    def fetchPage(self, pageNum):
        while True:
            try:
                url      = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
                requests = request.Request(url, headers=headers())
                response = request.urlopen(requests)
                html     = response.read().decode('utf-8')
                if '百度安全验证' in html:
                    print('百度安全验证，正在重新获取网页...')
                    time.sleep(random.randrange(2, 5) * 0.1)
                else:
                    return html
            except:
                print('连接失败')
                return None

    # 获取帖子的标题
    def fetchTitle(self):
        page    = self.fetchPage(1)
        pattern = re.compile(r'(?<=<title>).*(?=_百度贴吧)')
        result  = re.search(pattern, page)
        if result:
            return result.group()
        else:
            return f'获取标题失败'

    # 获取帖子的总页数
    def fetchTotalPage(self):
        page    = self.fetchPage(1)
        pattern = re.compile(r'(?<=共<span class="red">)\d*(?=</span>页)')
        result  = re.search(pattern, page)
        if result:
            totalPage = int(result.group())
            return totalPage
        else:
            return f'获取页数失败'

    # 查看楼层信息
    def fetchFloorInfo(self):
        pass


# 测试
if __name__ == '__main__':
    originURL = 'https://tieba.baidu.com/p/8101474840'
    post01    = BaiduTieBa(originURL, 0)

    print(post01.fetchPage(1))
