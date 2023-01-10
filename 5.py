# n = int(input('n: '))
# data = {i: {'name': input('name: '), 'email': input('email: ')} for i in range(n)}
# print(data)

# text = input()
# data = {i: text.count(i) for i in text}

# a = 3
# if a % 2:
#     print('odd')
#     print('odd')
# elif a == 0:
#     print('zero')
#     print('zero')
# else:
#     print('even')
#     print('even')

# a = int(input())
# # if a % 2:
# #     is_even = 'odd'
# # else:
# #     is_even = 'even'
#
# # is_even = 'odd' if a % 2 else 'even'
# print('odd' if a % 2 else 'even')

# x = True
# y = False
# z = False
# if not x or y:
#     print(1)
# elif not x or not y and z:
#     print(2)
# elif not x or y or not y and x:
#     print(3)
# else:
#     print(4)
# for number in range(1, 10, 2):
#     number = number ** 2
#     print(number, end=' ')
#

# words = ['hello', 'python', 'world']
# for word in words:
#     print(word)
# for i, elem in enumerate(words):
#     print(i, elem)
# for i in range(len(words)):
#     print(i)

# data = {
#     'name': 'vasya',
#     'email': 'vasya@info.com',
#     'age': 23
# }

# for key in data:
#     print(key)
# for val in data.values():
#     print(val)
# for key, val in data.items():
#     print(key, val)

# вводится произвольная строка, вывести из нее только буквы в верхнем регистре
# text = input('text: ')
# for elem in text:
#     if elem.isupper():
#         print(elem)

# for i in range(100):
#     if not i % 7:
#         continue
#     print(i)

# for i in range(10):
#     if i == 7:
#         break
#     print(i)
# print('finish!')

# for i in range(10):
#     if i == 7:
#         break
#     print(i)
# else:
#     print('закончился самостоятельно!')

# a = 2
# while a <= 1024:
#     a **= 2
#     print(a)

# дан список чисел, удалить из списка все 2 (while)
# numbers = [5, 12, 4, 2, 4, 21, 4, 2, 4, 2, 4, 2, 7, 8, 2]
# while 2 in numbers:
#     numbers.remove(2)
# print(numbers)


# спрашивать у пользователя данные с клавиатуры до тех пор, пока он не введет число
# number = input('enter number: ')
# while not number.isdigit():
#     number = input('are you stupid? try again: ')

# number1 = input()
# number2 = input()
# try:
#     number1 = int(number1)
#     number2 = int(number2)
#     number3 = number1 / number2
# except ValueError:
#     print('неверные данные')
# except ZeroDivisionError:
#     print('на 0 делить нельзя')

# number1 = input()
# number2 = input()
# try:
#     number1 = int(number1)
#     number2 = int(number2)
#     number3 = number1 / number2
# except ValueError:
#     print('value error')
# except Exception as e:
#     print(e)
# else:
#     print('ошибок не было')
# finally:
#     print('работает всегда')

# card_number = input()
# if not card_number.isdigit() or len(card_number) != 16:
#     raise ValueError('invalid card number')

# вводится число, посчитать сумму его цифр
# number = input('enter number: ')
# s = 0
# for i in number:
#     s += int(i)
# print(f'{s=}')
# numbers = []
# for i in range(1, 101):
#     if (i ** 2) % 5:
#         numbers.append(i**2)
# print(numbers)
#
# numbers = [i**2 for i in range(1, 101) if (i ** 2) % 5]

# N = int(input('N: '))
# M = int(input('M: '))
# K = int(input('K: '))
# start = (K // M) * M + M
# stop = start + M * N
# for i in range(start, stop, M):
#     print(i)
# numbers = []
# while len(numbers) < N:
#     if not K % M:
#         numbers.append(K)
#         K += M
#     else:
#         K += 1
# print(numbers)

# N = int(input('N: '))
# M = int(input('M: '))
# for i in range(2, N+1, 2):
#     print(i, end=' ')
#     if not i % 10:
#         print()

# c = 0
# for i in range(2, N+1, 2):
#     c += 1
#     if c > M:
#         c = 1
#         print()
#     print(i, end=' ')

# 2 4 6 8 10
# 12 14 16 18 20
# 22 24 26 28 30
# 32 34 36 38 40
# for i in range(2, N + 1, 10):
#     for j in range(i, i+9, 2):
#         if j <= N:
#             print(j, end=' ')
#         else:
#             break
#     print()

# from itertools import zip_longest
# numbers = [i for i in range(2, N+1, 2)]
# numbers_iter = iter(numbers)
# numbers = list(zip_longest(*([numbers_iter]*5)))
# for line in numbers:
#     print(line)
