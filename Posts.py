import BaiduTieBa as BDTB
import re
import time
import random


class Posts(BDTB.BaiduTieBa):
    def __init__(self, baseURL, seeLZ):
        super().__init__(baseURL, seeLZ)

    # 获取回复帖内容(仅文字)
    def fetchComments(self):
        page                   = BDTB.BaiduTieBa.fetchPage(self)
        extractPostPattern     = re.compile(r'(?<=content " style="display:;">\s{20}).*(?=</div><br>)')
        rmLabelPattern         = re.compile(r'<.*>')
        unextractedPostsList   = re.findall(extractPostPattern, page)
        textList               = filter(lambda text: re.sub(rmLabelPattern, '', text), unextractedPostsList)
        """ 相当于:
        textList = []
        for text in unextractedPostsList:
            res = re.sub(rmLabelPattern, '', text)
            testList.append(res)
        """
        return list(textList)

    # 获取楼中楼内容
    def fetchCommentsReply(self):
        pass


# 测试
if __name__ == '__main__':
    originURL = 'https://tieba.baidu.com/p/8218780207?frwh=index'
    post01    = Posts(originURL, 0)
    method    = [post01.fetchTitle, post01.fetchTotalPage]

    for i in method:
        print(i())
        time.sleep(random.randrange(1, 3) * 0.1)
    print()
    print(post01.fetchComments())
