from BaiduTieBa import *


class Posts(BaiduTieBa, Tools):
    def __init__(self, baseURL, seeLZ):
        super().__init__(baseURL, seeLZ)

    # 获取回复帖内容
    def fetchComments(self, page):
        extractPostPattern     = re.compile(r'(?<=content " style="display:;">\s{20}).*(?=</div><br>)|'
                                            r'(?<=content\s\sclearfix" style="display:;">\s{12}).*(?=</div><br>)')
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

    # 打印所有回复帖
    @staticmethod
    def printAllComments(pageNum, post):
        counter = 1
        for i in range(1, pageNum + 1):
            print(f'\n==================== 正在获取第{i}页数据 ====================')
            page = post.fetchPage(i)
            comments = post.fetchComments(page)
            for comment in comments:
                print(f'\n—————————— {counter}楼 ——————————')
                print(comment)
                counter += 1
