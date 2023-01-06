# import sqlite3
#
#
# conn = sqlite3.connect('db.sqlite3')
# cur = conn.cursor()
#
#
# # cur.execute('''
# # CREATE TABLE IF NOT EXISTS categories(
# #     id INTEGER PRIMARY KEY AUTOINCREMENT,
# #     name VARCHAR(32) NOT NULL UNIQUE,
# #     is_published BOOLEAN DEFAULT (true)
# # );
# # ''')
# # conn.commit()
# #
# # cur.execute(
# #     'CREATE TABLE IF NOT EXISTS products('
# #     'id INTEGER PRIMARY KEY AUTOINCREMENT,'
# #     'name VARCHAR(64) NOT NULL,'
# #     'descr VARCHAR(1024),'
# #     'price FLOAT NOT NULL DEFAULT (1),'
# #     'category_id INTEGER NOT NULL,'
# #     'FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE'
# #     ');'
# # )
# # conn.commit()
# #
# # # cur.execute('DROP TABLE products;')
# # # conn.commit()
#
# # cur.executemany('''
# #     INSERT INTO categories(name, is_published) VALUES (?, ?);
# # ''', (('Doping', True), ))
# # conn.commit()
#
# # cur.execute('''
# #     UPDATE categories SET is_published = ?, name = ?
# #     WHERE id = ?;
# # ''', (False, 'Meat', 6))
# # conn.commit()
#
# # cur.execute('''DELETE FROM categories WHERE is_published = ?;''', (False, ))
# # conn.commit()
#
# # cur.executemany('''
# #     INSERT INTO products(
# #         name, descr, price, category_id
# #     )
# #     VALUES (?, ?, ?, ?);
# # ''', (
# #     ('Doping', None, 10, 4),
# #     ('Coffee', 'Latte', 5, 5)
# # ))
# # conn.commit()
#
# # cur.execute('''
# #     SELECT name FROM categories WHERE is_published = ? ORDER BY name ASC;
# # ''', (True, ))
# # print(cur.fetchall())
# # cur.execute('''
# #     SELECT * FROM products WHERE category_id = 5 ORDER BY price ASC;
# # ''')
# # print(cur.fetchall())
#
# cur.execute('''
#     SELECT categories.name, products.name, products.descr, products.price
#     FROM categories
#     LEFT JOIN products
#     ON categories.id = products.category_id
#     WHERE categories.is_published = ?;
# ''', (True, ))
# print(cur.fetchall())

import psycopg2


conn = psycopg2.connect('postgresql://milvus:qwerty12345678@0.0.0.0:5432/bh63')
with conn:
    with conn.cursor() as cur:
        cur.execute('''
            CREATE TABLE IF NOT EXISTS products(
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) NOT NULL UNIQUE,
                descr VARCHAR(1024),
                category_id INTEGER NOT NULL,
                FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
            );
        ''')
        conn.commit()
        # cur.execute("INSERT INTO categories(name) VALUES ('Food');")
        # conn.commit()
        cur.execute('SELECT * FROM categories;')
        print(cur.fetchall())
conn.close()
