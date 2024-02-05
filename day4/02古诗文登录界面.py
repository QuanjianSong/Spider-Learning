'''
超级鹰的使用流程
    - 将验证码图片下载到本地
    - 调用api进行图片数据的识别
'''
from lxml import etree
import requests
from chaojiying import get_code_text



if __name__ == '__main__':
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    page_text = requests.get(url, headers=headers).text
    tree = etree.HTML(page_text)
    src_list = tree.xpath('/html/body/form[1]/div[4]/div[4]/img/@src')
    # breakpoint()
    src_url = 'https://so.gushiwen.org' + src_list[0]
    img_data = requests.get(src_url, headers=headers).content
    with open('./code.jpg', 'wb') as fp:
        fp.write(img_data)
    
    # 调用打码平台的实例数据：
    reuslt_json = get_code_text('./code.jpg')
    print(reuslt_json['pic_str'])
        
