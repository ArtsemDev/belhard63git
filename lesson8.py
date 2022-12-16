"""

"""


# # # # from typing import Any
# # # #
# # # #
# # # # def binary_search(elements: list[Any], element: Any) -> Any:
# # # #     start = 0
# # # #     end = len(elements) - 1
# # # #     while True:
# # # #         center = (end + start) // 2
# # # #
# # # #         if element == elements[center]:
# # # #             return center
# # # #
# # # #         if element > elements[center]:
# # # #             start = center
# # # #         else:
# # # #             end = center
# # #
# # #
# # class Person:
# #
# #     national = 'kirgiz'
# #
# #     def __init__(self, name: str, age: int) -> None:
# #         self.name = name.title()
# #         self.age = age
# #         self.city = 'Minsk'
# #
# #     def change_name(self, new_name: str) -> None:
# #         self.name = new_name.title()
# #
# #     @classmethod
# #     def change_national(cls, new_national: str) -> None:
# #         cls.national = new_national.title()
# #         # cls.country = 'Belarus'
# #
# #
# # vasya = Person(name='vasya', age=34)
# # petya = Person(name='petya', age=23)
# # # Person.change_national('belarus')
# # # # vasya.change_national('russian')
# # # # print(petya.national)
# # # # print(vasya.name)
# # # # print(petya.name)
# # # # Person.national = 'belarus'
# # # # Person.color = 'black'
# # # # print(vasya.national)
# # # # print(vasya.national)
# # # # vasya.city = 'minsk'
# #
# # # Описать класс User, конструктор класса принимает имя и возвраст пользователя
# # # Создать список эземпляров класса User и отсортировать по возрасту
# #
# #
class User:

    def __init__(self, name: str, age: int) -> None:
        if not isinstance(name, str):
            raise TypeError('argument `name` must be str')
        if not isinstance(age, int):
            raise TypeError('argument `age` must be int')
        if age < 6:
            raise ValueError('argument `age` must be great then 5')
        self.name = name.title()
        self.age = age
        self.i = -1

    def __len__(self) -> int:
        return self.age ** 2

    def __getitem__(self, item):
        return self.__getattribute__(item)

    def __str__(self):
        return f'User: name={self.name} age={self.age}'

    def __add__(self, other):
        if isinstance(other, int):
            self.age += other
            return self
        elif isinstance(other, User):
            return self.age + other.age

    def __radd__(self, other):
        return self.__add__(other)

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i < len(self.name):
            return self.name[self.i]
        else:
            raise StopIteration
#
#
# vasya = User(name='vasya', age=34)
# petya = User(name='petya', age=12)
# for i in petya:
#     print(i)
#
# # a = vasya + petya
# # print(vasya.age)
# # print(petya.age)
# # print(a)
# # print(vasya.__getattribute__('name'))
# # print(vasya['name'])
# #
# # users: list[User] = [
# #     User(name='vasya', age=34),
# #     User(name='petya', age=12),
# #     User(name='masha', age=23)
# # ]
# # users.sort(key=lambda x: x.age)
# # # [34, 12, 23]
# # print(users[0].name)
# # # print(users)
# # # for user in users:
# # #     print(user.name, user.age)


def multiply(a: float | int, b: float | int) -> float | int:
    """Произведение двух чисел

    :param a: первый множитель
    :param b: второй множитель
    :return: результат произведения
    """
    return a * b
