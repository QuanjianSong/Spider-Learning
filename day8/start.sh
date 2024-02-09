#! /bin/bash

# 参数
PROJECT_NAME=boss_project
SPIDER_NAME=boss

# 创建一个工程：
scrapy startproject $PROJECT_NAME
cd $PROJECT_NAME

#在spiders的子目录下创建一个爬虫文件：
scrapy genspider $SPIDER_NAME www.xxx.com

#执行工程：执行之前，记得把settings中的robot协议去掉。
# scrapy crawl $SPIDER_NAME # --nolog不打印日志, 不建议用，建议在setting中添加 LOG_LEVEL = 'ERROR'