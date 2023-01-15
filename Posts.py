from BaiduTieBa import *
import re


class Posts(BaiduTieBa, Tools):
    def __init__(self, baseURL, seeLZ):
        super().__init__(baseURL, seeLZ)

    # 获取回复帖内容
    def fetchComments(self, page):
        extractPostPattern     = re.compile(r'(?<=content " style="display:;">\s{20}).*(?=</div><br>)')
        unextractedPostsList   = re.findall(extractPostPattern, page)                    # 将初步筛选后的帖放进列表
        postsList              = [Tools.replace(self, p) for p in unextractedPostsList]  # 将完全筛选后的帖放进列表
        """ 测试 """
        # for i in unextractedPostsList:
        #     print(Tools.replace(self, i))
        #     print('—————— 分割线 ——————')
        return postsList

    # 获取楼中楼内容
    def fetchCommentsReply(self):
        pass


# 测试
if __name__ == '__main__':
    originURL = 'https://tieba.baidu.com/p/8218759311?frwh=index'
    post01    = Posts(originURL, 0)
    method    = [post01.fetchTitle, post01.fetchTotalPage]
    result    = []
    for m in method:
        result.append(m())
    result.append(post01.fetchComments(post01.fetchPage(1)))

    counter   = 1
    print()
    for i in result:
        if isinstance(i, list):
            for value in i:
                print(f'—————— {counter}楼 ——————')
                print(value)
                counter += 1
        else:
            print(i, '\n')
