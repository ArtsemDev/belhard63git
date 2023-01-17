# # from requests import Session
# #
# #
# # class YandexDiskAPI:
# #
# #     HEADERS = {
# #         'Authorization': ''
# #     }
# #
# #     def get_disk_info(self):
# #         with Session() as session:
# #             response = session.get(
# #                 url='https://cloud-api.yandex.net/v1/disk/',
# #                 headers=self.HEADERS
# #             )
# #             print(response.status_code)
# #             print(response.text)
# #             print(response.json())
# #
# #     def _put(self, url: str):
# #         with open('products.csv', 'r') as file:
# #             with Session() as session:
# #                 with session.put(
# #                     url=url,
# #                     headers=self.HEADERS,
# #                     data=file.read().encode()
# #                 ) as response:
# #                     print(response.status_code)
# #
# #     def upload_file(self, path: str):
# #         with Session() as session:
# #             response = session.get(
# #                 url='https://cloud-api.yandex.net/v1/disk/resources/upload',
# #                 params={
# #                     'path': path
# #                 },
# #                 headers=self.HEADERS
# #             )
# #             if response.status_code == 200:
# #                 self._put(response.json().get('href'))
# #
# #
# # if __name__ == '__main__':
# #     api = YandexDiskAPI()
# #     api.upload_file('/Загрузки/products.csv')
# from requests import Session
#
#
# def get_response():
#     with Session() as session:
#         response = session.get(
#             url='https://api2.relax.by/?v=2.0&tree=searchTreeId&method=navigation.getSearchMenu'
#         )
#         print(response.status_code)
#
#
# if __name__ == '__main__':
#     import threading
#     import multiprocessing
#     threads = [multiprocessing.Process(target=get_response) for _ in range(100)]
#     for thread in threads:
#         thread.start()

# for _ in range(100):
#     get_response()
# import asyncio
# from aiohttp import ClientSession
#
#
# async def get_response():
#     async with ClientSession() as session:
#         response = await session.get(
#             url='https://api2.relax.by/?v=2.0&tree=searchTreeId&method=navigation.getSearchMenu'
#         )
#         print(response.status)
#
#
# async def main():
#     loop = asyncio.get_running_loop()
#     tasks = [loop.create_task(get_response()) for _ in range(100)]
#     for task in tasks:
#         await task
#
#
# if __name__ == '__main__':
#     asyncio.run(main())
