# a = 1234
# b = 3456
# text = 'first=%d second=%d' % (a, b)
# print(text)
# text2 = 'first=' + str(a) + ' second=' + str(b)
# print(text2)
# text3 = 'first={} second={}'.format(a, b)
# print(text3)
# text4 = f'first={a} second={b}'
# print(text4)

# name = 'Alex'
# age = 34
# text = f'Hello {name}, your age {age}'
# print(text)

# text = 'hello---world---python---hello'
# words = text.split('---')
# print(words)
# text = '|'.join(words)
# print(text)

# text = 'hello python hello'
# print(text.rfind('Hello', 0, 10))

# text = 'hello python world python world'
# print(text.rpartition('Python'))

# text = '<b>hello world python</b>'
# text = text.replace('<b>', '')
# text = text.replace('</b>', '')
# print(text)
# text = '56789'
# print(text.istitle())


# text = 'hel\tlo\tpyt\thon'
# text2 = 'hey\twor\tld'
# print(text.expandtabs(15))
# print(text2.expandtabs(15))

# text = '...---===hello \tworld-=.-=.'
# print(text.lstrip('.-='))
# print(text.rstrip('.-='))
# print(text.strip('.-='))


# text = 'hello world'
# print(text.removeprefix('hell').removesuffix('rld'))
# print(text.removesuffix('rld'))
# text = 'hello'
# print(text.center(11))
# print(text.zfill(10))

# print(bin(10)[2:].zfill(8))
# print(bin(10)[2:].ljust(100000, '-'))
# print(bin(10)[2:].rjust(8, '-'))

# print(bin(78))
# print(bin(88))
# print(bin(78 ^ 88))
#
# print(bin(10))
# print(bin(10 << 3))
# print(bin(10 >> 2))

# text = 'hello python'
# a = 'hello'
# b = 'hello'
# print(a is b)
# print(id(a))
# print(id(b))

# a = 0.3
# b = round(0.1 * 3, 1)
# print(a)
# print(b)
# print(id(a))
# print(id(b))

# пользователь вводит предложение с клавиатуры,
# состоящее минимум из
# трех слов, переставить местами первое и
# последнее слово
# text = 'hello python world'
# first = text[:text.find(' ')]
# last = text[text.rfind(' ') + 1:]
# center = text[text.find(' '): text.rfind(' ') + 1]
# text = last + center + first
# print(text)
# words = text.split()
# words[0], words[-1] = words[-1], words[0]
# text = ' '.join(words)
# print(text)


# дано трехзначное число, вывести каждую его цифру
# по отдельности и найти сумму его цифр
number = input()
first = int(number[0])
second = int(number[1])
third = int(number[2])
print(first)
print(second)
print(third)
print(first + second + third)
# numbers = list(map(int, list(number)))
# print(*numbers)
# print(sum(numbers))
