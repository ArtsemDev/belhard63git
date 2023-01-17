# import threading
# import multiprocessing
#
#
# def main(i):
#     from time import sleep
#     for _ in range(10):
#         print(i)
#         sleep(1)
#
#
# if __name__ == '__main__':
#     threads = [multiprocessing.Process(target=main, args=(i, )) for i in range(10)]
#     for thread in threads:
#         thread.start()
#
import asyncio


async def ping(i):
    from asyncio import sleep
    for _ in range(10):
        print(i)
        await sleep(1)


async def main():
    loop = asyncio.get_running_loop()
    tasks = [loop.create_task(ping(i)) for i in range(10)]
    for task in tasks:
        await task


class Foo:

    i = 0

    @staticmethod
    def create_decorator(func):
        async def wrapper(*args, **kwargs):
            return await func(*args, **kwargs)

        return wrapper

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.i < 10:
            self.i += 1
            return self.i
        else:
            self.i = 0
            raise StopAsyncIteration


async def foo():
    obj = Foo()
    async for i in obj:
        print(i)


if __name__ == '__main__':
    # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(foo())
