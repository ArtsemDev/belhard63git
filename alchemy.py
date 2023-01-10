# # category = Category()[1]
# # print(category)
# from abc import ABC
# from pprint import pprint
#
# from models import Category, Base
#
# # category = Category(name='Doping', is_published=False)
# # category.save()
#
# # category = Category.get(2)
# # category.is_published = True
# # category.save()
#
# # categories = Category.all(is_published = True)
# # print(categories)
#
# # category = Category.get(3)
# # category.delete()
#
# #
# # cat = Category()
# # for category in cat(is_published=True):
# #     print(category.name)
#
#
# # with _Session() as session:
# #     category = Category(name='Drinks')
# #     session.add(category)
# #     session.commit()
# #     session.refresh(category)
# #     print(category.id)
#
# # products = [
# #     {
# #         'title': 'Food 1',
# #         'descr': 'Descr 1',
# #         'price': 100,
# #         'category_id': 1
# #     },
# #     {
# #         'title': 'Food 2',
# #         'descr': 'Descr 2',
# #         'price': 150,
# #         'category_id': 1
# #     },
# #     {
# #         'title': 'Drinks 1',
# #         'descr': 'Descr 3',
# #         'price': 50,
# #         'category_id': 2
# #     },
# #     {
# #         'title': 'Drinks 2',
# #         'descr': 'Descr 4',
# #         'price': 75,
# #         'category_id': 2
# #     }
# # ]
# # for product in products:
# #     product = Product(**product)
# #     product.save()
#
# # with _Session() as session:
# #     # category = session.get(Category, 2)
# #     # print(category.__dict__)
# #     categories = session.scalars(
# #         select(Category).filter_by(is_published=True).order_by('name')
# #     )
# #     print(categories.all())
# # SELECT * FROM categoris JOIN products ON categories.id = products.category_id WHERE categoris.is_published = True;
# #     response = session.execute(
# #         select(Category, Product)
# #         .join(Product, Category.id == Product.category_id)
# #         .where(Category.is_published.is_(True))
# #     )
# #     for category, product in response.all():
# #         print(category.name, product.title)
#
# # with _Session() as session:
# #     product = session.get(Product, 3)
# #     session.delete(product)
# #     session.commit()
# # session.execute(delete(Product).where(Product.id == 4))
# # session.commit()
#
# # with _Session() as session:
# # session.execute(
# #     update(Category)
# #     .where(Category.id == 2)
# #     .values(name='Coffee')
# # )
# # session.commit()
# # category = session.get(Category, 2)
# # category.name = 'Drinks'
# # category.is_published = False
# # session.add(category)
# # session.commit()
#
#
# # response = Category.join(right=Product)
# # print(response)
#
# # from csv import DictWriter
# #
# # categories = Category.all()
# # categories = list(map(lambda x: x.dict(), categories))
# # keys = list(categories[0].keys())
# #
# # with open('categories.csv', 'w', encoding='utf-8') as file:
# #     writer = DictWriter(file, fieldnames=keys)
# #     writer.writeheader()
# #     writer.writerows(categories)
#
# # Product.load_csv('products.csv', 'w')
#
# # from models import Category
# #
# #
# # categories = [
# #     ('Cat1', None),
# #     ('Cat2', None),
# #     ('Cat3', 1),
# #     ('Cat4', 2),
# #     ('Cat5', 1),
# #     ('Cat6', 4)
# # ]
# # for category in categories:
# #     category = Category(name=category[0], parent_id=category[1])
# #     category.save()
#
#
# data = [
#     {
#         'name': 'Cat1',
#         'subcategories': [
#             {
#                 'name': 'Cat3'
#             },
#             {
#                 'name': 'Cat5'
#             }
#         ]
#     },
#     {
#         'name': 'Cat2',
#         'subcategories': [
#             {
#                 'name': 'Cat4',
#                 'subcategories': [
#                     {
#                         'name': 'Cat6'
#                     }
#                 ]
#             }
#         ]
#     }
# ]
#
#
# # def category_recursive_serializer(parent_id: int = None) -> list[dict]:
# #     # json = []
# #     categories = Category.all(parent_id=parent_id)
# #     # if categories:
# #     #     for category in categories:
# #     #         data = {
# #     #             'name': category.name
# #     #         }
# #     #         response = category_recursive_serializer(category.id)
# #     #         if response:
# #     #             data['subcategories'] = response
# #     #         json.append(data)
# #
# #     json = [
# #         {
# #             'name': category.name,
# #             'subcategories': category_recursive_serializer(category.id),
# #         }
# #         for category in categories
# #     ]
# #     return json
# #
# #
# # pprint(category_recursive_serializer())
#
#
# def paginator(page: int, paginate_by: int) -> list[str]:
#     categories = Category.all(order_by='id', limit=paginate_by, offset=page*paginate_by)
#     return [category.name for category in categories]
#
#
# class Paginator(ABC):
#     model: Base = None
#     paginate_by: int = 5
#     order_by: str = 'id'
#
#     @classmethod
#     def get_queryset(cls, page: int) -> list[Base]:
#         return cls.model.all(order_by=cls.order_by, limit=cls.paginate_by, offset=(page-1)*cls.paginate_by)
#
#     @classmethod
#     def page(cls, page: int) -> list[str]:
#         return [obj.dict() for obj in cls.get_queryset(page=page)]
#
#     @classmethod
#     def pages(cls) -> list[list[str]]:
#         page = 0
#         pages = []
#         while True:
#             _page = cls.page(page)
#             if _page:
#                 pages.append(_page)
#                 page += 1
#             else:
#                 break
#         return pages
#
#
# class CategoryPaginator(Paginator):
#     model = Category
#     paginate_by = 2
#
#
# # category_paginator = CategoryPaginator()
# # print(category_paginator.pages())
# # print(CategoryPaginator.page(1))


def dispatcher():
    registry = []

    def filters(**kwargs):
        def wrapper(func):
            registry.append({'func': func, 'filters': kwargs})

            def decorator(**kwargs):
                return func(**kwargs)

            return decorator

        return wrapper

    filters.all = registry
    return filters


# class Dispatcher(object):
#
#     def __call__(self, *args, **kwargs):
#         registry = []
#
#         def filters(self, **kwargs):
#             def wrapper(self, func):
#                 registry.append({'func': func, 'filters': kwargs})
#
#                 def decorator(self, **kwargs):
#                     return func(**kwargs)
#
#                 return decorator
#
#             return wrapper
#
#         filters.all = registry
#         return filters
#
#     def run(self, data):
#         for func in dp.all:
#             for key, val in func.get('filters').items():
#                 if key not in data:
#                     break
#                 if data.get(key) != val:
#                     break
#             else:
#                 func['func'](**data)
#
#
dp = dispatcher()


@dp(a=5, b=4)
def foo(**kwargs):
    print('foo')


@dp(a=5)
def baz(**kwargs):
    print('baz')


@dp(c=6, d=7, e=8)
def bar(**kwargs):
    print('bar')


def main(data):
    for func in dp.all:
        for key, val in func.get('filters').items():
            if key not in data:
                break
            if data.get(key) != val:
                break
        else:
            func['func'](**data)


if __name__ == '__main__':
    # dp.run({'a': 5, 'b': 7, 'e': 8, 'f': 9})
    main({'a': 5, 'd': 7, 'e': 8, 'f': 9})
