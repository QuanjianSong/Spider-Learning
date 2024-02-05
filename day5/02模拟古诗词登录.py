'''
验证码的识别，获取验证码图片的文字数据
'''
import requests
from lxml import etree
from chaojiying import get_code_text


if __name__ == '__main__':
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }
    session = requests.Session()
    response = session.get(url, headers=headers)
    if response.status_code == 200:
        page_text = response.text
        tree = etree.HTML(page_text)
        img_src = tree.xpath('/html/body/form[1]/div[4]/div[4]/img/@src')[0]

        full_src = 'https://so.gushiwen.cn/' + img_src
        src_data = session.get(full_src, headers=headers).content
        with open ('code.jpg', 'wb') as fp:
            fp.write(src_data)

        # 调用打码平台的实例数据：
        reuslt_json = get_code_text('./code.jpg')
        print(reuslt_json['pic_str'])

        # 发送post请求模拟登录
        login_url = r'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
        data = {
            '__VIEWSTATE': '8rissbNxx5ZRGEKxDhGx14OihMZI4zmYcNiLEHEbk/ljLuEaElw8dmvmACCUNIQMzJgtqcdLWyFyccuxfW8wiOVixmt1670hxgbYBEke1D0NBxdZy1X1GoeHL4xTGMzTW/nH0sPcoMemmRf+JjCE+FSYNWo=',
            '__VIEWSTATEGENERATOR': 'C93BE1AE',
            'from': 'http://so.gushiwen.cn/user/collect.aspx',
            'email': '862553420@qq.com',
            'pwd': '100867292a',
            'code': reuslt_json['pic_str'],
            'denglu': '登录'
        }
        # 请求个人信息
            # login_headers = {
            #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
            #     "Cookie": 'xxxx';
            # }
        login_response = session.post(login_url, headers=headers, data=data)
        if login_response.status_code == 200:
            print("successful!")
            login_page_text = login_response.text
            with open('./gushici.html', 'w', encoding='utf-8') as fp:
                fp.write(login_page_text)
        else:
            print("failed!")
    else:
        print(response)
        print("连接失败")