什么是框架？
    就是一个集成了很多功能并且具有很强通用性的一个项目模型

如何学习一个框架？
    专门学习框架封装的各种功能的详细用法。

功能：
    高性能的持久化存储
    异步的数据下载
    高性能的数据解析

安装
    pip install scrapy

创建一个工程：
    scrapy startproject xxxpro
    cd 工程目录

在spiders的子目录下创建一个爬虫文件：
    scrapy genspider spider_name(名字) www.xxx.com

执行工程：
    执行之前，记得把settings中的robot协议去掉。
    scrapy crawl spider_name(名字) --nolog # nolog不打印日志, 不建议用，建议在setting中添加 LOG_LEVEL = 'ERROR'

注意：UA伪装也在settings里面。

数据解析的操作
    参数response可以直接调用.xpath
    .xpath返回是一个列表，每个元素是一个Selector对象，可以调用.extract()方法获取文本

持久化操作：
    基于终端指令
        只可以将parse方法返回值存储到本地的文本文件中
        scrapy crawl spider_name(名字) -o lujings.jsonl
        输出只能为json,jsonl,csv,xml，局限性较强
    基于管道
        - 编码流程：
            - 数据解析
            - 在item类中定义相关的属性
            - 将解析的数据封装到Item类型对象中（利用item作为中介）
            - 将item类型的对象提交到管道进行持久化的操作
            - 在管道类的process_item中要将其接受到的item对象存储到数据库中（数据存储写在这里）
            - 在配置文件中开启管道
