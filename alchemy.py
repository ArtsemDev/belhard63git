from models import Category, Product, User

# category = Category()[1]
# print(category)

# category = Category(name='Doping', is_published=False)
# category.save()

# category = Category.get(2)
# category.is_published = True
# category.save()

# categories = Category.all(is_published = True)
# print(categories)

# category = Category.get(3)
# category.delete()

#
# cat = Category()
# for category in cat(is_published=True):
#     print(category.name)


# with _Session() as session:
#     category = Category(name='Drinks')
#     session.add(category)
#     session.commit()
#     session.refresh(category)
#     print(category.id)

# products = [
#     {
#         'title': 'Food 1',
#         'descr': 'Descr 1',
#         'price': 100,
#         'category_id': 1
#     },
#     {
#         'title': 'Food 2',
#         'descr': 'Descr 2',
#         'price': 150,
#         'category_id': 1
#     },
#     {
#         'title': 'Drinks 1',
#         'descr': 'Descr 3',
#         'price': 50,
#         'category_id': 2
#     },
#     {
#         'title': 'Drinks 2',
#         'descr': 'Descr 4',
#         'price': 75,
#         'category_id': 2
#     }
# ]
# for product in products:
#     product = Product(**product)
#     product.save()

# with _Session() as session:
#     # category = session.get(Category, 2)
#     # print(category.__dict__)
#     categories = session.scalars(
#         select(Category).filter_by(is_published=True).order_by('name')
#     )
#     print(categories.all())
# SELECT * FROM categoris JOIN products ON categories.id = products.category_id WHERE categoris.is_published = True;
#     response = session.execute(
#         select(Category, Product)
#         .join(Product, Category.id == Product.category_id)
#         .where(Category.is_published.is_(True))
#     )
#     for category, product in response.all():
#         print(category.name, product.title)

# with _Session() as session:
#     product = session.get(Product, 3)
#     session.delete(product)
#     session.commit()
    # session.execute(delete(Product).where(Product.id == 4))
    # session.commit()

# with _Session() as session:
    # session.execute(
    #     update(Category)
    #     .where(Category.id == 2)
    #     .values(name='Coffee')
    # )
    # session.commit()
    # category = session.get(Category, 2)
    # category.name = 'Drinks'
    # category.is_published = False
    # session.add(category)
    # session.commit()


# response = Category.join(right=Product)
# print(response)

# from csv import DictWriter
#
# categories = Category.all()
# categories = list(map(lambda x: x.dict(), categories))
# keys = list(categories[0].keys())
#
# with open('categories.csv', 'w', encoding='utf-8') as file:
#     writer = DictWriter(file, fieldnames=keys)
#     writer.writeheader()
#     writer.writerows(categories)

# Product.load_csv('products.csv', 'w')
Category.upload_csv('categories.csv')
