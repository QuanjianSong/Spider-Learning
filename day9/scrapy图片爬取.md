专门用于图片爬取的ImagesPipeline类
    基于scrapy爬取字符串类型数据和爬取图片类型数据的区别
        字符串：只需要基于xptah进行解析并且封装成item提交给管道。
        图片：xpath只能先解析出图片的src地址，单独对图片地址再进行请求获取二进制类型的数据，再封装成item提交给管道。
    ImagePipeline类：
        只需要将img的src属性值进行解析，提交到管道，管道自动对图片进行下载，并且将下载后的图片进行保存。
    需求：爬取站长素材中的高清图片。
    使用流程：
        数据解析
        将存储图片的地址的item提交到指定的管道类中
        自己编写一个pipeline的类，继承ImagesPipeline，重写三个方法：
            get_media_requests：模拟请求发送
            file_path：指定图片的名称
            item_completed：图片下载完成后的return item
        在配置文件中：
            需要制定图片的存储目录：IMAGES_STORE='./imgs'
            指定开启的管道。

    困难：
        图片懒加载
