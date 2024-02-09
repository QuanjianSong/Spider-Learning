CrawSpider类，Spider的一个子类
    全站数据爬取的方式
        基于Spider: 手动请求
        基于CrawSpider: 自动请求
    CrawSpider的使用：
        创建一个工程：scrapy startproject xxxpro
        cd XXX
        创建爬虫文件 （CrawlSpider）
            scrapy genspider -t crawl www.xxx.com
        核心组建：
            链接提取器：
                作用：根据指定的规则（allow），进行指定的链接提取
                Rule（
            规则解析器：
                将链接提取器指定对应的规则（回调函数）进行解析
