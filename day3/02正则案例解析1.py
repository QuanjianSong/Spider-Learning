'''
用正则进行数据解析
需求：爬取糗事百科中所有的图片
'''
import re
import requests


if __name__ == '__main__':
    url = 'https://movie.douban.com/typerank?type_name=喜剧&type=24&interval_id=100:90&action='
    # 进行ua伪装
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        page_text = response.text
        print(page_text)

        # 使用聚焦爬虫将页面中的所有图片解析
        '''
        <div class="movie-list-item playable unwatched"><div class="movie-content"><a href="https://movie.douban.com/subject/1292063/" target="_blank"><img data-original="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2578474613.jpg" class="movie-img" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2578474613.jpg" style="display: block;"></a><div class="movie-info"><div class="movie-name"><span class="movie-name-text"><a href="https://movie.douban.com/subject/1292063/" target="_blank">美丽人生</a></span><span class="playable-sign">[可播放]</span><span class="rank-num">1</span></div><div class="movie-crew">罗伯托·贝尼尼 / 尼可莱塔·布拉斯基 / 乔治·坎塔里尼 / 朱斯蒂诺·杜拉诺 / 赛尔乔·比尼·布斯特里克 / 玛丽萨·帕雷德斯 / 霍斯特·布赫霍尔茨 / 利迪娅·阿方西 / 朱利亚娜·洛约迪切 / 亚美利哥·丰塔尼 / 彼得·德·席尔瓦 / 弗朗西斯·古佐 / 拉法埃拉·莱博罗尼 / 克劳迪奥·阿方西 / 吉尔·巴罗尼 / 马西莫·比安奇 / 恩尼奥·孔萨尔维 / 吉安卡尔洛·科森蒂诺 / 阿伦·克雷格 / 汉尼斯·赫尔曼 / 弗兰科·梅斯科利尼 / 安东尼奥·普雷斯特 / 吉娜·诺维勒 / 理查德·塞梅尔 / 安德烈提多娜 / 迪尔克·范登贝格 / 奥梅罗·安东努蒂 / 沈晓谦 / 张欣</div><div class="movie-misc">2020 / 意大利 / 剧情 / 喜剧 / 爱情 / 战争</div><div class="movie-rating"><span class="bigstar50"></span><span class="rating_num">9.5</span><span class="comment-num">1359913人评价</span></div></div></div></div>
        '''
        ex = """class="movie-list-panel pictext" """
        # 正则表达式
        img_list = re.findall(ex, page_text, re.S) # re.S单行匹配
        print(img_list)


    else:
        print("响应失败")
