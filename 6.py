# # # FIFO - First In First Out
# # # LIFO - Last In First Out
# #
# # # def multiply(a, *b, c=4, d=None, **kwargs):
# # #     print(a)
# # #     print(b)
# # #     print(c)
# # #     print(d)
# # #     print(kwargs)
# # #
# # #
# # # e = 'hello'
# # # multiply(1, e, 6, 7, d=8, name='vasya', age='23')
# #
# # # def foo(b, a=None):
# # #     if a is None:
# # #         a = []
# # #     a.append(b)
# # #     print(a)
# # #
# # #
# # # foo(4)
# # # foo(4)
# #
# # # идемпотентной
# # # a = 4
# # # def foo():
# # #     a = 5
# # #     def bar():
# # #         nonlocal a
# # #         print(a)
# #
# #
# # # def multiply(a, b):
# # #     print(a * b)
# # #
# # #
# # # text = 'multiply'
# # #
# # # globals().get(text)(6, 7)
# #
# # # def foo():
# # #     print('foo')
# # #
# # #
# # # def bar():
# # #     print('bar')
# # #
# # #
# # # def baz():
# # #     print('baz')
# # #
# # #
# # # def error():
# # #     print('error')
# # #
# # #
# # # a = int(input())
# # # data = {
# # #     1: foo,
# # #     2: bar,
# # #     3: baz,
# # # }
# # # data.get(a, error)()
# #
# #
# # # multiply = lambda a, b: a * b
# # # print(multiply(3, 4))
# #
# #
# # # lst = [4, 5, 6, 'hellooo', 5, 'python', 'world', 'age', 4, 3, 5]
# # # lst.sort(key=lambda x: x if isinstance(x, int) else len(x))
# # # print(lst)
# #
# # # написать функцию сортировки списка строк в лексическом (алфавитном) порядке
# # # words = ['AGE', 'apple', 'WOMAN', 'man', 'Dog', 'dUCK']
# # # words.sort(key=lambda x: x.upper())
# # # print(words)
# #
# # # numbers = ['1', '3', '5', '7']
# # # numbers = tuple(map(lambda x: int(x) ** 2, numbers))
# # # print(numbers)
# # # data = {
# # #     'key1': '1',
# # #     'key2': '2',
# # #     'key3': '3'
# # # }
# # #
# # # data = dict(map(lambda x: (x[0], int(x[1])), data.items()))
# # # print(data)
# #
# # # words = ['hello', '', 'python', 'age', '', '1234']
# # # words = list(filter(lambda x: x.isalpha(), words))
# # # print(words)
# # #
# # # def foo(a):
# # #     def bar(b):
# # #         return a * b
# # #     return bar
# #
# #
# # # c = foo(3)
# # # d = foo(9)
# # # print(c(8))
# # # print(c(4))
# # # print(d(5))
# # # print(d(6))
# # # print(foo(2)(8))
# #
# # # def foo(a):
# # #     def bar(b):
# # #         def baz(c):
# # #             return a * b * c
# # #         return baz
# # #     return bar
# # #
# # #
# # # print(foo(3)(4)(5))
# #
# # # users = [
# # #     {
# # #         'name': 'name1',
# # #         'email': 'email1'
# # #     },
# # #     {
# # #         'name': 'name2',
# # #         'email': 'email2'
# # #     },
# # #     {
# # #         'name': 'name3',
# # #         'email': 'email3'
# # #     },
# # #     {
# # #         'name': 'name4',
# # #         'email': 'email4'
# # #     },
# # #     {
# # #         'name': 'name5',
# # #         'email': 'email5'
# # #     },
# # #     {
# # #         'name': 'name6',
# # #         'email': 'email6'
# # #     },
# # #
# # # ]
# # #
# # #
# # # def get_users(start, stop):
# # #     for i in range(start, stop):
# # #         yield users[i]
# # #
# # #
# # # for _ in get_users(2, 4):
# # #     print(_)
# # # from sys import getrecursionlimit, setrecursionlimit
# # # print(getrecursionlimit())
# # # setrecursionlimit(2000)
# # # print(getrecursionlimit())
# #
# #
# # # numbers = [3, 4, 5, 6, [5, 4, 6, [3, 4, 2, 0], 5, 6, 4, ], 6, 7, 4, [3, 4, 5, 3, [6, 7, 8, [8, 9, 6]]], 4, 5, 32, 5, 2]
# # #
# # #
# # # def recursive_multiply(numbers):
# # #     c = 1
# # #     for el in numbers:
# # #         if isinstance(el, (int, float)):
# # #             c *= el if el else 1
# # #         elif isinstance(el, (list, tuple)):
# # #             c *= recursive_multiply(el)
# # #     return c
# # #
# # #
# # # print(recursive_multiply(numbers))
# #
# # # def foo(a):
# # #     if a == 100:
# # #         return a
# # #     return foo(a + 1)
# # #
# # #
# # # print(foo(1))
# #
# #
# # # def is_numeric(func):
# # #     def wrapper(a, b):
# # #         if not isinstance(a, (int, float)):
# # #             raise TypeError
# # #         if not isinstance(b, (int, float)):
# # #             raise TypeError
# # #         result = func(a + 1, b + 2)
# # #         return f'{result=}'
# # #     return wrapper
# # #
# # #
# # # def multiply(a, b):
# # #     return a * b
# # #
# # #
# # # decorated_multiply = is_numeric(multiply)
# # #
# # #
# # # print(multiply(4, 5))
# # # print(decorated_multiply(4, 5))
# #
# # def my_decorator(a, b):
# #     def decorator(func):
# #         def wrapper(c, d):
# #             c += a
# #             d += b
# #             return func(c, d)
# #         return wrapper
# #     return decorator
# #
# #
# # @my_decorator(1, 2)
# # def multiply(a, b):
# #     return a * b
# #
# #
# # print(multiply(4, 5))
#
#
# def multiply(a: int | float, b: int | float) -> int | float:
#     return a * b
#
#
# a: int | float = multiply(4, 5)
# a += 1
# a: str = f'{a}'
#

a = 3 ** 4
b = str(a)
c = f'{a}'

