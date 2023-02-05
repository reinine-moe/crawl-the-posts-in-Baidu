#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Posts import *


# 测试
class Test:
    urlPattern = re.compile(r'^https://tieba.baidu.com/p/.*$')

    def matchUrl(self, url):
        return re.match(self.urlPattern, url)

    @staticmethod
    def isTrue(choice):
        return True if choice in ('1', '0') else False


# 主程序
def start():
    post        = Posts(originUrl, seeLZ)                # 保存信息
    initialPage = post.fetchPage(1)                      # 获取首页信息
    pageNum     = int(post.fetchTotalPage(initialPage))  # 获取总页数

    print('\n\n帖子标题：', post.fetchTitle(initialPage))
    print('帖子总页数：'  , pageNum)

    post.printAllComments(pageNum, post)

    time.sleep(0.5)
    input('\nenter any button to exit...')


originUrl = input('请输入帖子地址：\n')
seeLZ     = input('是否只获取楼主发言，是输入1，否输入0：\n')
test      = Test()

# 符合条件则开始运行
if test.matchUrl(originUrl) and test.isTrue(seeLZ):
    start()
else:
    print('请正确填写网址及其他选项')
