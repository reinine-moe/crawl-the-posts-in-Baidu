from urllib import request


class BaiduTieBa:
    def __init__(self, baseURL, seeLZ):
        self.baseURL = baseURL
        self.seeLZ   = '?see_lz=' + str(seeLZ)

    def fetchPage(self):
        page     = request.urlopen(self.baseURL + self.seeLZ,)
        response = page.read().decode('utf-8')
        return response


if __name__ == '__main__':
    url      = 'https://tieba.baidu.com/p/6802656129'
    headers  = {'User-Agent'     : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                   'Chrome/108.0.0.0 Safari/537.36',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
                'Accept'         : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;'
                                   'q=0.8,application/signed-exchange;v=b3;q=0.9'
                }
    requests = request.Request(url, headers=headers)
    post01   = BaiduTieBa(url, 0)
    print(post01.fetchPage())
