# # # numbers = [1, 2, 'hello', 4, 5]
# # # print(numbers[2])
# # # print(numbers[2:4])
# # # # numbers[2] = 3
# # # # print(numbers)
# # # print(numbers[2][1])
# # # print(len(numbers))
# # # print(list('hello'))
# # # from random import randint
# # # numbers = [randint(1, 10) for i in range(10)]
# # # print(numbers)
# #
# # # words = ['hello', 'python', 'world', 'python', 'pycharm']
# # # words.remove('python')
# # # print(words)
# # # a = words.pop(2)
# # # print(words)
# # # print(a)
# #
# #
# # # numbers = [1, 2, 3, 4]
# # # numbers.append('hello')
# # # numbers.insert(1, 'new')
# # # print(numbers)
# # numbers1 = [1, 2, 3, 4]
# # numbers2 = [5, 6, 7, 8]
# # numbers3 = numbers1 + numbers2
# # # numbers1.extend(numbers2)
# # print(numbers1 * 3)
# # print(numbers2)
# # print(numbers3)
#
# # numbers = [4, 8, 7, 5, 4, 3, 6, 2, 3, 8, 6, 4, ]
# # # numbers.sort(reverse=True)
# # numbers_sort = sorted(numbers, reverse=True)
# # print(numbers)
# # print(numbers_sort)
#
# # numbers = ['hello', 'Python', 'apple', 'bread', 'World', [2, 5, 3, 6, 7]]
# # numbers[5].sort()
# # print(numbers)
#
# # numbers = [1, 2, 3, 4, 5]
# # numbers.reverse()
# # numbers_reversed = numbers[::-1]
# # numbers.clear()
# # numbers = []
# # numbers = list()
# # print(numbers)
# # numbers = [1, 2, 3, 4]
# # numbers2 = [numbers, 5, 6, 7]
# # numbers2[0].append('new')
# # print(numbers)
#
# # number = (5, )
#
# # numbers = (1, 2, 3, 4, [5, 6, 7, 8])
# # numbers[4].append(9)
# # numbers.count(2)
# # print(numbers)
# # new_number = numbers + numbers * 3
# # print(new_number)
# # words = {'hello', 'python', 'world', 'pycharm'}
# # print(words)
#
# # s = {i**2 for i in range(1, 10)}
# # print(s)
# # s2 = {5, 3, 6, 8, 2, 5, 3, 6}
# # print(s2)
# # s1 = {3, 6, 5, 4}
# # s2 = {8, 2, 6, 2, 0}
# # s3 = {1, 2, 3, 4, 5, 9, 8, }
# # s4 = s1 | s2 | s3
# # print(s4)
#
# # s1 = {1, 2, 3, 4, 5, 6, }
# # s2 = {4, 5, 6, 7, 8}
# # s4 = {5, 4, 8, 9}
# # s3 = s1 & s2 & s4
# # print(s3)
#
# # user = {
# #     'name': 'vasya',
# #     'age': 34,
# #     'is_human': True
# # }
# # print(user['age'])
# # user['age'] = 23
# # user['city'] = 'minsk'
# # print(user)
#
# # user = [['name', 'vasya'], ['age', 23]]
# # user = dict(user)
# # print(user.setdefault('city', 'Н/У'))
# # print(user)
# # print(user)
#
# # keys = ['name', 'age', 'city']
# # user = dict.fromkeys(keys, None)
# # print(user)
# # user = {
# #     'name': 'vasya'
# # }
# # print(user.popitem())
# # print(user)
# # age = user.pop('age', None)
# # print(age)
# # user = {
# #     'name': 'vasya',
# #     'age': 23
# # }
# # user2 = {
# #     'age': 32,
# #     'city': 'minsk'
# # }
# # # user.update(user2)
# # user3 = user | user2
# # print(user3)
# #
# # numbers = (7, 4, 6, 2, 8, -12, -56, 3, 4)
# # numbers2 = [5, 6, 3, 5, 3]
# # print(min(numbers))
# # print(sum(numbers))
# # words = ['hello', 'python', 'world', 'hell', 'Apply', 'app']
# # print(min(words))
#
# from collections import Counter, deque, namedtuple, ChainMap
#
#
# # text = 'hello world'
# # text2 = 'python'
# # count = Counter(text)
# # count2 = Counter(text2)
# # print(list(count.elements()))
# # print(count.most_common(2))
# # print(count)
# # print(count2)
# # count.subtract(count2)
# # print(count)
# # text = 'hello'
# # data = {i: i for i in text}
# # print(data)
#
# # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# # q = deque(numbers, 4 // 2)
# # print(q)
#
# # keys = ['name', 'age', 'city']
# # User = namedtuple('User', keys)
# # vasya = User('vasya', 23, 'minsk')
# # petya = User('petya', 32, 'brest')
# #
# # print(vasya.name)
# # print(petya.age)
# # print(vasya._asdict())
#
# data1 = {
#     'a': 1,
#     'b': 2
# }
# data2 = {
#     'b': 3,
#     'c': 4
# }
# chain = ChainMap(data1, data2)
# # data1['c'] = 5
# print(chain['c'])
# chain['e'] = 6
# print(data1)
# print(data2)
