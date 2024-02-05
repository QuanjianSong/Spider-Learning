import asyncio


async def request(url):
    print("正在请求的url是,", url)
    print("请求成功,", url)
    return url

# 回调函数
def callback_func(task):
    # .result 表示任务对象中封装的协程对应函数的返回值
    print(task.result())


if __name__ == '__main__':
    c = request('www.baidu.com')

    # # 创建一个事件循环对象
    # loop = asyncio.get_event_loop()

    # # 将协程对象注册到loop中, 并启动
    # loop.run_until_complete(c)

    # ------------task的使用--------------
    # loop = asyncio.get_event_loop()
    # # 创建一个task
    # task = loop.create_task(c)
    # print(task)
    # # 将task对象注册到loop中，并启动
    # loop.run_until_complete(task)
    # print(task)

    # ------------feature的使用--------------
    # loop = asyncio.get_event_loop()

    # feature = asyncio.ensure_future(c)
    # print(feature)
    # loop.run_until_complete(feature)
    # print(feature)

    # ------------绑定回调---------------
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(c)
    # 将回调函数绑定到任务对象中
    task.add_done_callback(callback_func)

    loop.run_until_complete(task)

