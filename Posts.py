import BaiduTieBa as BDTB
from urllib import request
import re
import time
import random


class Posts(BDTB.BaiduTieBa):
    def __init__(self, baseURL, seeLZ):
        super().__init__(baseURL, seeLZ)

    # 获取回复帖内容
    def fetchComments(self):
        page = BDTB.BaiduTieBa.fetchPage(self)

    # 获取楼中楼内容
    def fetchCommentsReply(self):
        pass


if __name__ == '__main__':
    originURL = 'https://tieba.baidu.com/p/8211167248?frwh=index'
    post01    = Posts(originURL, 0)
    method    = [post01.fetchTitle, post01.fetchTotalPage]

    for i in method:
        print(i())
        time.sleep(random.randrange(1, 3) * 0.1)
