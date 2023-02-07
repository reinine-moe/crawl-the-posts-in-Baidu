# 贴吧爬虫

reiNine 2023/2/7




## 主要思路&解决方法

我将这个小项目分为了四个部分，分别为：

- **[BaiduTieBa.py](https://github.com/reinine-y/crawl-the-posts-in-Baidu/blob/main/BaiduTieBa.py)**
    - 在这一部分中主要分为两个类，分别为 `Tools` 和 `BaiduTieBa` ，其中 `Tools` 的作用在于剔除多余的标签并只显示出我们想要的结果；而 `BaiduTieBa` 的主要作用是获取帖子的各种基本信息（如标题与页数）。当网络服务器返回安全验证的响应时，通过更改请求头的相关信息来重新获取网页。

- **[Post.py](https://github.com/reinine-y/crawl-the-posts-in-Baidu/blob/main/Posts.py)**
    - 这一部分的功能原本是获取回复帖内容，并打印输出回复帖和楼中楼的所有内容，最后在本地保存。结果因为太懒了很多东西都没有完成，只是简单的输出了回复帖的内容。

- **[headers.py](https://github.com/reinine-y/crawl-the-posts-in-Baidu/blob/main/headers.py)**
    - 由于贴吧的反爬虫机制，大量的访问与刷新页面会导致安全验证。为了减少安全验证，我使用了github中其他大佬的成果： [curlconverter](https://github.com/curlconverter/curlconverter) ，也参考了[其他人](https://github.com/diskcat/tiebaSpider/blob/master/readme.md)使用手机热点的解决方法，并在请求头中随机更换Cookie，以此来减少安全验证的次数。当然虽然有用但算不上特别好。

- **[main.py](https://github.com/reinine-y/crawl-the-posts-in-Baidu/blob/main/main.py)**
    - 这一部分是主程序，包括了简单的测试和程序本体，原本在这个部分还想在写一个装饰器来充当日志的作用，最后也是因为懒没有实现。。。

除此之外，我在获取网页时也遇到了如果遇上了安全验证会重复打印一段话的小问题，主要是这段话会一直刷屏很影响美观，于是我就想做一个等待条的效果，这样能够更直观的显示。虽然在网上没有找到一样的效果，但是我还是根据了一个[跟我想象中比较相近的做法](https://blog.csdn.net/zhouhua2022/article/details/124516239)来修改成了我自己想要的结果：
```py
import time

point = '.'
counter = 1

while True:
    print('\rloading', point * counter, end='')
    counter += 1
    if counter == 4:
        counter = 1
    time.sleep(0.5)
```




## 碎碎念

不得不说寒假确实闲得慌，因为最近贴吧逛得比较多，有时候在帖子内容比较多的情况下，想要找到自己想要的信息确实是比较麻烦的 ~~（绝对不是因为想找涩图和资源）~~，恰好这段时间稍微自学了一点git方面的知识，同时想要了解一下一个项目是怎么样进行的（当然我还是知道在正式的项目中是没有这么简单和不规范的），于是乎便开始尝试的想要做一下人生中的第一个小项目。

然而并没有想象中的那么容易，因为要考虑的东西实在是比较多，导致一时间不知道该如何下手。稍微码了十几行之后感觉方向有点问题，于是便去网上看了看有没有类似的思路。

最后在阅读完这篇[文章](https://blog.csdn.net/qq_38887171/article/details/109197736)后确定的思路，正好也尝试了下之前写小脚本时没有用到的面向对象的形式。

### 优点：

额，能够勉强算的上优点的大概只有执行力比较强，在有了想法之后能能够快速地执行；然后就是有简单的代码分类，比较好维护（如果还会继续写的话）；学习能力不错，有不懂的只是能及时百度，并能够稍微地举一反三。

### 不足：

这次的不足显然是有很多的：

- 拖延症严重，原本认真搞个两三天就能完成的事，硬是被我拖了大半个月才完成；
- 三分钟热度，很多原本想要完成的功能都没有实现；
- 单线程，在帖子页数多的情况获取速度堪忧；
- 没有任何存储手段，只有一个简单的输出终端的功能，极其简陋