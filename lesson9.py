# # # # # # # class Transport(object):
# # # # # # #
# # # # # # #     def __init__(self, weight: int, color: str, power: int, name: str) -> None:
# # # # # # #         self.name = name
# # # # # # #         self.power = power
# # # # # # #         self.color = color
# # # # # # #         self.weight = weight
# # # # # # #
# # # # # # #     def __str__(self) -> str:
# # # # # # #         return self.name
# # # # # # #
# # # # # # #     def dict(self) -> dict:
# # # # # # #         return {
# # # # # # #             'name': self.name,
# # # # # # #             'power': self.power,
# # # # # # #             'color': self.color,
# # # # # # #             'weight': self.weight
# # # # # # #         }
# # # # # # #
# # # # # # #
# # # # # # # class Car(Transport):
# # # # # # #
# # # # # # #     def __init__(self, weight: int, color: str, power: int, name: str, max_speed: int):
# # # # # # #         super().__init__(weight, color, power, name)
# # # # # # #         self.max_speed = max_speed
# # # # # # #
# # # # # # #     def dict(self) -> dict:
# # # # # # #         data = super().dict()
# # # # # # #         data['max_speed'] = self.max_speed
# # # # # # #         return data
# # # # # #
# # # # # #
# # # # # # # class Car:
# # # # # # #
# # # # # # #     def beep(self):
# # # # # # #         print('beep-beep')
# # # # # # #
# # # # # # #
# # # # # # # class Moto:
# # # # # # #
# # # # # # #     def beep(self):
# # # # # # #         print('wrum-wrum')
# # # # # # #
# # # # # # #
# # # # # # # def beep(obj: Car | Moto):
# # # # # # #     obj.beep()
# # # # # #
# # # # # #
# # # # # # class A:
# # # # # #
# # # # # #     __private_attr = 'private'
# # # # # #
# # # # # #     def info(self):
# # # # # #         print(self.__private_attr)
# # # # # #
# # # # # #
# # # # # # class B(A):
# # # # # #
# # # # # #     def foo(self):
# # # # # #         print(self.__private_attr)
# # # # #
# # # # #
# # # # # class User:
# # # # #
# # # # #     def __init__(self, card_number: str):
# # # # #         self.__card_number = card_number
# # # # #
# # # # #     @property
# # # # #     def card_number(self):
# # # # #         return self.__card_number[-4:]
# # # # #
# # # # #     @card_number.setter
# # # # #     def card_number(self, value):
# # # # #         if not isinstance(value, str):
# # # # #             raise TypeError
# # # # #         if not value.isdigit():
# # # # #             raise ValueError
# # # # #         if len(value) != 16:
# # # # #             raise ValueError
# # # # #         self.__card_number = value
# # # # #
# # # # #
# # # # # vasya = User(card_number='1234567898762657')
# # # # # vasya.card_number = '9876987698769876'
# # # # # print(vasya.card_number)
# # # #
# # # #
# # # # class User:
# # # #
# # # #     def __init__(self, name: str, age: int):
# # # #         self.name = name.title()
# # # #         self.age = age
# # # #         self.is_active = True
# # # #
# # # #     def __str__(self) -> str:
# # # #         return self.name
# # # #
# # # #     def birthday(self) -> None:
# # # #         self.age += 1
# # # #
# # # #
# # # # class Group:
# # # #
# # # #     def __init__(self, users: list[User]) -> None:
# # # #         self.users = users
# # # #
# # # #     def birthday(self):
# # # #         for user in self.users:
# # # #             user.birthday()
# # # #
# # # #
# # # # users = [User(name=f'name{i}', age=i) for i in range(10)]
# # # # group = Group(users=users)
# # # # group.birthday()
# # #
# # # from abc import ABC, abstractmethod
# # #
# # #
# # # class User(ABC):
# # #
# # #     @classmethod
# # #     @abstractmethod
# # #     def foo(cls):
# # #         pass
# # #
# # #     def bar(self):
# # #         print('bar')
# # #
# # #
# # # class Person(User):
# # #
# # #     @classmethod
# # #     def foo(cls):
# # #         print('foo')
# # #
# # #
# # # vasya = Person()
# # # vasya.bar()
# #
# # from dataclasses import dataclass
# #
# #
# # @dataclass
# # class User:
# #     name: str
# #     age: int
# #     email: str
# #     city: str = 'Minsk'
# #
# #
# # class Manager(User):
# #     salary: int
# #
# #
# # vasya = User(name='vaysa', age=23, email='vasya@info.com')
# # petya = User(name='petya', age=56, email='petya@info.com', city='Brest')
# # print(vasya.city)
# # print(petya.city)
#
# # from enum import Enum
# #
# #
# # class HttpStatus(int, Enum):
# #     OK: int = 200
# #     PageNotFound: int = 404
# #     MethodNotAllowed: int = 405
# #
# #
# # status = 405
# #
# # if status == HttpStatus.MethodNotAllowed:
# #     pass
# from enum import Enum
#
#
# class Roles(int, Enum):
#     User: int = 1
#     Manager: int = 2
#     Admin: int = 3
#
#
# user = {
#     'name': 'vasya',
#     'email': 'vasya@info.com',
#     'role_id': 2
# }
#
# if user['role_id'] == Roles.Admin:
#     pass


class Car(object):
    
    def __init__(self, count_passenger_seat: int, is_baby_seat: bool, color: str) -> None:
        self.color = color
        self.count_passenger_seat = count_passenger_seat
        self.is_baby_seat = is_baby_seat
        self.is_busy = False

    def __str__(self) -> str:
        return f'Car {self.count_passenger_seat=} {self.is_baby_seat=} {self.is_busy=} {self.color=}'

        
class Taxi(object):

    def __init__(self, cars: list[Car]):
        self.cars = cars

    def find_car(self, count_passenger: int, is_baby: bool) -> Car | None:
        if is_baby:
            cars = list(filter(lambda x: not x.is_busy and x.is_baby_seat, self.cars))
        else:
            cars = list(filter(lambda x: not x.is_busy, self.cars))
        for car in cars:
            if car.count_passenger_seat >= count_passenger:
                car.is_busy = True
                return car
