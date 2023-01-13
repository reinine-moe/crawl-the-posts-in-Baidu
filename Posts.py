from BaiduTieBa import *
import re
import time
import random


class Posts(BaiduTieBa, Tools):
    def __init__(self, baseURL, seeLZ):
        super().__init__(baseURL, seeLZ)

    # 获取回复帖内容(仅文字)
    def fetchComments(self):
        page                   = BaiduTieBa.fetchPage(self)
        extractPostPattern     = re.compile(r'(?<=content " style="display:;">\s{20}).*(?=</div><br>)')
        unextractedPostsList   = re.findall(extractPostPattern, page)  # 将初步筛选后的回复帖放进列表
        for i in unextractedPostsList:
            print(Tools.replace(self, i))
            print('—————— 分割线 ——————')

    # 获取楼中楼内容
    def fetchCommentsReply(self):
        pass


# 测试
if __name__ == '__main__':
    originURL = 'https://tieba.baidu.com/p/8101474840'
    post01    = Posts(originURL, 0)
    method    = [post01.fetchTitle, post01.fetchTotalPage, post01.fetchComments]

    for i in method:
        print(i())
        time.sleep(random.randrange(1, 3) * 0.1)

