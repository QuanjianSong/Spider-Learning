import time
import asyncio
import aiohttp # 使用aiohttp的ClientSession

async def request(url):
    print('正在下载：', url)
    url = 'https://www.baidu.com/'
    # 在异步协程中如果出现了同步模块的代码，则无法实现异步。
    # time.sleep(2)
    # 遇到阻塞操作要手动刮起
    await asyncio.sleep(2)

    # request发送请求是同步的，需要使用基于异步的网络请求模块， 用aiohttp
    async with aiohttp.ClientSession() as session:
        # 可以使用headers、params、data等等数据，以及代理ip proxy='http://ip:port', 与proxies不一样
        async with await session.get(url) as response:
            # text()返回字符串的响应数据
            # read()返回二进制的响应数据
            # json()返回json的对象
            # 在获取响应数据之前，这边一定要await
            page_text = await response.text()

    
    print('下载结束：', url)
    return url


if __name__ == '__main__':
    urls = [
        'www.baidu.com',
        'www.sogou.com',
        'www.goubanjia.com'
    ]
    start = time.time()

    # 多任务采用任务列表，存放任务
    stasks = []
    for url in urls:
        c = request(url)
        task = asyncio.ensure_future(c)
        stasks.append(task)

    loop = asyncio.get_event_loop()

    # 需要将任务列表封装到wait中
    loop.run_until_complete(asyncio.wait(stasks))

    print(time.time() - start)